"""Tests for the read-only market-data clients.

All HTTP is stubbed with the ``requests_mock`` fixture -- these never touch the
network, so they are safe to run in CI / restricted environments. They cover
URL construction, cursor pagination, the retry wiring, and the typed-empty
DataFrame contract.
"""

from __future__ import annotations

import pytest

import kalshi_api
import polymarket_api


def test_kalshi_get_trades_paginates(requests_mock):
    url = f"{kalshi_api.BASE_URL}/markets/trades"
    requests_mock.get(
        url,
        [
            {"json": {"trades": [{"t": 1}, {"t": 2}], "cursor": "abc"}},
            {"json": {"trades": [{"t": 3}], "cursor": None}},
        ],
    )
    df = kalshi_api.get_market_trades("KXFED-26MAR", pause_s=0)
    assert len(df) == 3
    assert requests_mock.call_count == 2
    # second request should carry the cursor from the first page
    assert "cursor=abc" in requests_mock.request_history[1].url


def test_kalshi_list_markets_builds_request(requests_mock):
    requests_mock.get(f"{kalshi_api.BASE_URL}/markets", json={"markets": [{"ticker": "X"}]})
    df = kalshi_api.list_markets(series_ticker="KXFED")
    assert list(df["ticker"]) == ["X"]
    assert "series_ticker=KXFED" in requests_mock.last_request.url


def test_polymarket_price_history_empty_returns_typed_frame(requests_mock):
    requests_mock.get(f"{polymarket_api.CLOB_URL}/prices-history", json={"history": []})
    df = polymarket_api.get_price_history("tok123")
    assert list(df.columns) == ["date", "yes_price"]
    assert df.empty


def test_polymarket_price_history_parses_records(requests_mock):
    requests_mock.get(
        f"{polymarket_api.CLOB_URL}/prices-history",
        json={"history": [{"t": 1735689600, "p": "0.42"}]},
    )
    df = polymarket_api.get_price_history("tok123")
    assert list(df.columns) == ["date", "yes_price"]
    assert df.iloc[0]["yes_price"] == pytest.approx(0.42)


def test_both_sessions_have_retry_configured():
    for session in (kalshi_api._SESSION, polymarket_api._SESSION):
        adapter = session.get_adapter("https://example.com")
        retry = adapter.max_retries
        assert retry.total == 5
        assert 429 in retry.status_forcelist
