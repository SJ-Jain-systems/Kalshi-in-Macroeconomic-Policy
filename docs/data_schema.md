# Data schemas for real pulls

The notebooks ship with synthetic generators so they run offline. When you flip
`USE_REAL_DATA = True` (notebooks 02/03) or swap the generator in notebook 01,
the real data must match the shapes below — these are exactly what the
`src/` helpers consume. `data/` is gitignored; put raw/processed pulls there.

## 1. Per-strike "Yes" price series → `candlesticks_to_daily_ladder`

`kalshi_utils.candlesticks_to_daily_ladder` expects a
`dict[float, pandas.DataFrame]` mapping each **strike threshold** to a frame
with (at least) a date column and a daily "Yes" price:

| column | dtype | meaning |
|--------|-------|---------|
| `date` | datetime64 / parseable | one row per day |
| `yes_price` | float in `[0, 1]` | daily "Yes" price = P(outcome exceeds this strike) |

- The dict keys are the strikes (e.g. `4.00, 4.25, 4.50`); they need not be sorted.
- Days on which *any* strike lacks a price are dropped (a partial ladder can't be
  converted without imputation).
- Build it from Kalshi by looping strike markets in an event, calling
  `kalshi_api.get_market_candlesticks`, and reducing each candle to its daily
  close. Column names are configurable via `price_col` / `date_col`.

Output frame: one row per fully-populated day with columns
`['date', 'mean', 'median', 'mode', 'variance', 'skewness']` — the same contract
the synthetic generator in notebook 01 emits and `forecast_error_by_horizon`
consumes.

## 2. Kalshi raw endpoints (`src/kalshi_api.py`)

- `list_markets` / `list_events` → DataFrames of the raw `markets` / `events`
  arrays (fields per Kalshi's schema; `ticker` is the key column).
- `get_market_trades` → one row per trade (cursor-paginated).
- `get_market_candlesticks` → OHLC-style candles per market; reduce `close` (or
  the relevant price field) to the `yes_price` used above.

> Verify field names and the live/historical endpoint split against
> https://docs.kalshi.com before a large pull — see the caveat at the top of
> `kalshi_api.py`.

## 3. Polymarket (`src/polymarket_api.py`) → same ladder shape

- `search_markets(query)` / `list_event_markets(slug)` → market metadata
  (question, outcomes, `clobTokenId`, volume, liquidity, resolution).
- `get_price_history(clob_token_id)` → normalized `['date', 'yes_price']`,
  droppable straight into `candlesticks_to_daily_ladder`.
- `fed_ladder_from_markets(markets)` → the `{strike: DataFrame[date, yes_price]}`
  dict, after you map each sibling YES/NO market to a numeric strike (the
  judgement call flagged as a confound in `paper/sections/5`).

## 4. Notebook 02 volume frame

Notebook 02's liquidity plot expects a wide DataFrame indexed by date with one
column per series, each holding **daily traded volume** (contracts or dollars).
The synthetic generator produces ~180 trading days; a real pull should match
that shape (DatetimeIndex × series columns, float values).
