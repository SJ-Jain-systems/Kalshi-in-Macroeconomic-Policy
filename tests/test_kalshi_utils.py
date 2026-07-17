"""Unit tests for the probability-distribution core in ``kalshi_utils``.

These exercise the FEDS Section-3 ladder-to-pdf conversion, the day-by-day
ladder assembly, and the Figure-1 forecast-error helper. They are pure and
deterministic -- no network, no synthetic RNG.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

import kalshi_utils as ku


class TestLadderToPdf:
    def test_pmf_matches_consecutive_yes_diffs(self):
        strikes = [1.0, 2.0, 3.0]
        yes = [0.9, 0.6, 0.2]
        dist = ku.ladder_to_pdf(strikes, yes)
        # below-first = 1-0.9; between = 0.9-0.6, 0.6-0.2; above-last = 0.2
        np.testing.assert_allclose(dist.pmf, [0.1, 0.3, 0.4, 0.2], atol=1e-12)
        assert dist.pmf.sum() == pytest.approx(1.0)

    def test_symmetric_ladder_mean_and_median(self):
        strikes = [4.00, 4.25, 4.50]
        yes = [0.75, 0.50, 0.25]  # symmetric around 4.25
        dist = ku.ladder_to_pdf(strikes, yes)
        assert dist.mean == pytest.approx(4.25, abs=1e-12)
        assert dist.median == pytest.approx(4.25, abs=1e-12)

    def test_interpolated_median_is_sub_strike(self):
        # CDF crosses 0.5 partway through a bin -> median must land off the midpoint.
        strikes = [4.00, 4.25, 4.50]
        yes = [0.90, 0.40, 0.10]
        dist = ku.ladder_to_pdf(strikes, yes)
        # pmf = [0.1, 0.5, 0.3, 0.1]; cum before crossing bin = 0.1, mass 0.5
        # median = 4.00 + (0.5-0.1)/0.5 * 0.25 = 4.20
        assert dist.median == pytest.approx(4.20, abs=1e-12)
        # the naive bin-midpoint would have been 4.125 -- confirm we improved on it
        assert abs(dist.median - 4.125) > 1e-3

    def test_requires_increasing_strikes(self):
        with pytest.raises(ValueError):
            ku.ladder_to_pdf([2.0, 1.0], [0.5, 0.4])

    def test_requires_equal_length(self):
        with pytest.raises(ValueError):
            ku.ladder_to_pdf([1.0, 2.0, 3.0], [0.5, 0.4])

    def test_clips_and_renormalizes_nonmonotone_prices(self):
        # A non-monotone "Yes" ladder implies negative mass; it must be clipped
        # to zero and the pmf renormalized back to 1.
        strikes = [1.0, 2.0, 3.0]
        yes = [0.5, 0.6, 0.1]
        dist = ku.ladder_to_pdf(strikes, yes)
        assert (dist.pmf >= 0).all()
        assert dist.pmf.sum() == pytest.approx(1.0)


class TestCandlesticksToDailyLadder:
    @staticmethod
    def _frame(dates, prices):
        return pd.DataFrame({"date": pd.to_datetime(dates), "yes_price": prices})

    def test_assembles_and_drops_partial_days(self):
        two_days = ["2026-01-01", "2026-01-02"]
        candles = {
            4.00: self._frame(two_days, [0.80, 0.75]),
            4.25: self._frame(two_days, [0.50, 0.45]),
            4.50: self._frame(["2026-01-01"], [0.20]),  # 2026-01-02 missing
        }
        out = ku.candlesticks_to_daily_ladder(candles)
        assert list(out.columns) == ["date", "mean", "median", "mode", "variance", "skewness"]
        # only the fully-populated day survives
        assert len(out) == 1
        assert pd.Timestamp(out.iloc[0]["date"]) == pd.Timestamp("2026-01-01")

    def test_empty_input_raises(self):
        with pytest.raises(ValueError):
            ku.candlesticks_to_daily_ladder({})

    def test_missing_columns_raises(self):
        bad = {4.0: pd.DataFrame({"day": [1], "price": [0.5]})}
        with pytest.raises(ValueError):
            ku.candlesticks_to_daily_ladder(bad)


class TestForecastErrorByHorizon:
    def test_with_date_column(self):
        df = pd.DataFrame(
            {
                "date": pd.to_datetime(["2026-03-01", "2026-03-10"]),
                "mean": [4.10, 4.24],
            }
        )
        out = ku.forecast_error_by_horizon(
            df, realized_value=4.25, event_date=pd.Timestamp("2026-03-20")
        )
        assert list(out.columns) == ["days_before_event", "abs_error"]
        assert out["days_before_event"].tolist() == [19, 10]
        np.testing.assert_allclose(out["abs_error"].tolist(), [0.15, 0.01], atol=1e-9)

    def test_with_datetime_index(self):
        idx = pd.to_datetime(["2026-03-01", "2026-03-10"])
        df = pd.DataFrame({"mean": [4.10, 4.24]}, index=idx)
        out = ku.forecast_error_by_horizon(df, 4.25, pd.Timestamp("2026-03-20"))
        assert out["days_before_event"].tolist() == [19, 10]
