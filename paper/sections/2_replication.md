# 2. Replication

*Status: validation section. The goal is to confirm the FEDS paper's core
result on independently-pulled data, not to improve on it.*

## What to replicate

1. **Figure 1 — FOMC fed funds rate forecast error by days-before-meeting.**
   Kalshi mean/median/mode forecast error vs. fed funds futures error vs.
   SME median-of-modal-path error. Baseline pipeline is in
   `notebooks/01_figure1_replication.ipynb` (currently synthetic data —
   swap in a real pull via `src/kalshi_api.py`).
2. **Table 3 — forecast accuracy vs. benchmarks.** MAE/RMSE for headline
   CPI, core CPI, and unemployment (Kalshi mean/median/mode vs. Bloomberg
   consensus), and MAE/RMSE for the fed funds rate (Kalshi vs. fed funds
   futures), with Diebold-Mariano significance tests. The FEDS paper's
   headline result to reproduce: Kalshi median/mode significantly beat
   Bloomberg on headline CPI MAE (0.063 vs 0.081), and Kalshi median/mode
   have essentially zero error vs. fed funds futures' 0.010 MAE by the day
   of the FOMC meeting.

## Data gaps to solve

- **Kalshi trade-level data**: public via the API (`src/kalshi_api.py`),
  no special access needed.
- **NY Fed Survey of Market Expectations**: published PDFs per FOMC cycle
  (modal path + distribution), not point-in-time downloadable — will need
  manual/scraped ingestion of the SME summary PDFs.
- **Bloomberg consensus**: proprietary (Bloomberg terminal access). If
  unavailable, substitute a comparably-timed public consensus source (e.g.
  a different aggregator) and note the substitution explicitly — don't
  silently swap data sources into a "reproduction."
- **Fed funds futures settlement data**: CME data, may require a paid feed
  for historical intraday; end-of-day settlement prices are often
  sufficient for this comparison since the FEDS paper's own use is
  low-frequency (daily).

## What "success" looks like

A re-plotted Figure 1 on your own pull that qualitatively matches the FEDS
paper's shape (errors shrinking as the FOMC meeting approaches; Kalshi
median/mode reaching ~zero error near the meeting date; broad overlap with
the SME's one-half-standard-deviation band). Exact numeric match isn't the
bar — the FEDS paper's window, exact vendor cut for Bloomberg, and precise
SME PDF vintage may differ from what you can access.
