# Data-placeholder tracker

Every `[DATA PLACEHOLDER]` in the section drafts is a spot where a real number
or a source-verified citation must be swapped in. This table maps each one to
the notebook / data pull (or research task) that produces it, so the "what's
left to make this a real paper" state is legible at a glance.

Follow the "Suggested order of work" in the README; fill the rows in that order.

| # | Location (`file:line`) | What it needs | Filled by | Status |
|---|------------------------|---------------|-----------|--------|
| 1 | `paper/sections/1_background.md:40` | FEDS instrument-comparison table (OIS/TIPS/SME vs. Kalshi) | Literature/source verification against the FEDS paper | ☐ |
| 2 | `paper/sections/2_replication.md:43` | Re-plotted Figure 1 on an independent Kalshi pull | Notebook 01 on real fed funds rate series (`USE_REAL_DATA`) | ☐ |
| 3 | `paper/sections/2_replication.md:58` | Reproduced Table 3 accuracy numbers | Notebook 01 + NY Fed SME / fed funds futures baselines | ☐ |
| 4 | `paper/sections/3_manipulation_risk.md:51` | Per-thin-series cost-to-move dollar estimates | Notebook 02 (trailing volume / OI vs. $7M cap) | ☐ |
| 5 | `paper/sections/3_manipulation_risk.md:63` | Trailing volume / open interest per series | Notebook 02 real pull | ☐ |
| 6 | `paper/sections/3_manipulation_risk.md:74` | CFTC enforcement precedent (needs source verification) | Research task | ☐ |
| 7 | `paper/sections/4_institutional_pathway.md:71` | Specific FOMC-minutes / speech citations (needs source verification) | Research task | ☐ |
| 8 | `paper/sections/4_institutional_pathway.md:85` | Any formal Fed use of market-implied measures (needs source verification) | Research task | ☐ |
| 9 | `paper/sections/4_institutional_pathway.md:102` | "Sourced to" column, verified citations | Research task | ☐ |
| 10 | `paper/sections/5_polymarket_comparison.md:29` | Inventory of overlapping Polymarket FOMC/macro markets | Notebook 03 via `polymarket_api.search_markets` | ☐ |
| 11 | `paper/sections/5_polymarket_comparison.md:44` | Side-by-side Figure 1 (Kalshi vs. Polymarket) | Notebook 03 real pull | ☐ |
| 12 | `paper/sections/5_polymarket_comparison.md:60` | Per-platform accuracy metric values + event windows | Notebook 03 real pull | ☐ |
| 13 | `paper/sections/6_policy_recommendation.md:40` | Numeric safeguard threshold from Section 3 evidence | Derived from rows 4–5 once filled | ☐ |

Line numbers are current as of this tracker's creation; re-grep with
`grep -rn "DATA PLACEHOLDER" paper/sections/` if the drafts have since moved.
