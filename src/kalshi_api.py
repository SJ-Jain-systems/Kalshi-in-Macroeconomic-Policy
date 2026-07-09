"""
Minimal client for Kalshi's public market-data REST API.

Market-data endpoints (series, events, markets, trades, candlesticks) are
publicly readable without authentication or fees. Trading/portfolio
endpoints require an API key with RSA-PSS request signing, which this
module does not implement (not needed for read-only research use).

IMPORTANT: Kalshi's API has changed over time, most recently splitting
market data into separate "live" and "historical" endpoint tiers
(effective February 2026) and moving rate limiting to a token-bucket model
(effective April 2026). Verify current paths and params against
https://docs.kalshi.com before relying on this for anything beyond a
prototype -- the endpoint templates below reflect the general v2 REST
structure (/trade-api/v2/...) but exact query parameters and the
live/historical split are worth double-checking.
"""

from __future__ import annotations

import time

import pandas as pd
import requests

BASE_URL = "https://api.kalshi.com/trade-api/v2"


def _get(path: str, params: dict | None = None) -> dict:
    resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


def get_series(series_ticker: str) -> dict:
    """e.g. series_ticker='KXFED' for fed funds rate, verify actual tickers via /series"""
    return _get(f"/series/{series_ticker}")


def list_events(series_ticker: str | None = None, status: str | None = None) -> pd.DataFrame:
    params = {}
    if series_ticker:
        params["series_ticker"] = series_ticker
    if status:
        params["status"] = status
    data = _get("/events", params=params)
    return pd.DataFrame(data.get("events", []))


def list_markets(event_ticker: str | None = None, series_ticker: str | None = None) -> pd.DataFrame:
    params = {}
    if event_ticker:
        params["event_ticker"] = event_ticker
    if series_ticker:
        params["series_ticker"] = series_ticker
    data = _get("/markets", params=params)
    return pd.DataFrame(data.get("markets", []))


def get_market_trades(ticker: str, max_pages: int = 20, pause_s: float = 0.2) -> pd.DataFrame:
    """
    Pull trade-level history for a single market ticker, paginating via the
    API's cursor. This is the trade-level data underlying the FEDS paper's
    strike-ladder-to-pdf conversion (see src/kalshi_utils.ladder_to_pdf).
    """
    all_trades = []
    cursor = None
    for _ in range(max_pages):
        params = {"ticker": ticker, "limit": 1000}
        if cursor:
            params["cursor"] = cursor
        data = _get("/markets/trades", params=params)
        trades = data.get("trades", [])
        all_trades.extend(trades)
        cursor = data.get("cursor")
        if not cursor or not trades:
            break
        time.sleep(pause_s)
    return pd.DataFrame(all_trades)


def get_market_candlesticks(series_ticker: str, ticker: str, start_ts: int, end_ts: int, period_interval: int = 1440) -> pd.DataFrame:
    """
    Daily (period_interval=1440 minutes) OHLC-style candles for a market --
    the fastest way to reconstruct a daily-updating "Yes" price series for
    an entire strike ladder without pulling every individual trade.
    """
    params = {"start_ts": start_ts, "end_ts": end_ts, "period_interval": period_interval}
    data = _get(f"/series/{series_ticker}/markets/{ticker}/candlesticks", params=params)
    return pd.DataFrame(data.get("candlesticks", []))
