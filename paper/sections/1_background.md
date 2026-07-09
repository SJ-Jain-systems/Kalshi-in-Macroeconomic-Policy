# 1. Background

*Status: framing section, short by design. Most of the substantive claims
here should just cite the FEDS paper directly rather than re-derive them.*

## What to establish

- Prediction markets as an expectations-measurement tool: surveys (SME,
  Bloomberg consensus, Blue Chip, SPF) vs. market-based measures (fed funds
  futures, SOFR options, OIS, CPI fixings, TIPS breakevens) vs. Kalshi. Pull
  the comparison table structure directly from the FEDS paper's Table 2 and
  cite it — don't rebuild it from scratch, just reproduce the frame and add
  a column for Polymarket (feeds section 5).
- Kalshi's regulatory status: CFTC-approved Designated Contract Market
  (DCM), same category as CME. Market makers (Susquehanna), retail access
  via Robinhood/Webull. This regulatory detail is the load-bearing fact for
  sections 3–5 (manipulation risk, institutional legitimacy, and the
  Polymarket comparison all hinge on "regulated exchange" status).
- Kalshi's market list relevant to macro policy (FEDS paper Table 1): CPI
  MoM/YoY/annual, core CPI MoM/YoY/annual, unemployment, payrolls, GDP
  growth (quarterly + annual), probability of US recession (annual), fed
  funds rate decision and target rate (per-FOMC-meeting).
- One paragraph stating this project's five-part extension (see root
  README) and how it maps to the `paper/sections/` files.

## Don't duplicate

Calibration methodology, the strike-ladder-to-pdf conversion, and the core
accuracy results (Figure 1, Table 3) belong in `2_replication.md` and the
notebooks — not here.
