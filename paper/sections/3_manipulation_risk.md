# 3. Manipulation and Market Integrity Risk

*Status: new section — the FEDS paper gives this one sentence (a citation
to Hanson and Oprea 2009, p.6). This section should be the empirical core
of the "should the Fed trust this" argument.*

## Facts already in the FEDS paper to build from

- Kalshi's **maximum exposure per market is $7 million** (p.8, "Competing
  Platforms"). This is presented as a liquidity/maturity advantage over
  Polymarket/PredictIt, but it's also the ceiling a manipulator would need
  to work within (or around, via multiple accounts).
- Kalshi fed funds rate contracts are demonstrably liquid: volumes
  "frequently above a million" in recent years, peaking near 100 million
  around a September FOMC meeting (Figure 3, p.12). This is the *most*
  liquid, most FOMC-attention-grabbing series on the platform.
- The paper gives **no equivalent volume figures for GDP growth, probability
  of recession, or core CPI annual** — series with much shorter listing
  histories (Table 1: core CPI-for-year started 2025, probability of
  recession started 2022 as an annual contract). These are the natural
  candidates for thin-market risk.
- Hanson and Oprea (2009): prediction markets can remain informative even
  in the presence of manipulation attempts, because manipulators effectively
  subsidize informed traders who trade against the distortion. This is a
  theoretical result about *equilibrium* robustness — it does not mean any
  individual pre-announcement snapshot is manipulation-proof, especially in
  a thin market with a short window (e.g., the 24–48 hours before an FOMC
  decision) where informed counter-trading may not have time to arrive.

## Research questions to answer with real data

1. **Cost-to-move estimate.** For the thinnest series in Table 1 (GDP
   growth, recession probability), what does the order book depth look
   like a day or two before a scheduled release? Estimate dollars required
   to move the implied probability by, say, 10 percentage points. Compare
   this dollar figure to (a) the $7M exposure cap and (b) the size of
   position a bank, hedge fund, or PAC could plausibly and legally take.
2. **Does the $7M cap bind where it matters?** It may be irrelevant for the
   FFR market (where hundred-million-dollar volumes make $7M a rounding
   error) but highly binding — or trivially evadable via multiple accounts
   — in a thin GDP or recession market where $7M could be most of total
   open interest.
3. **Regulatory backstop.** Kalshi's DCM status subjects it to CFTC
   oversight, including large-trader reporting and market-manipulation
   enforcement authority that does not apply to Polymarket. Research: has
   the CFTC taken any manipulation-related enforcement action against a DCM
   prediction market? What's the actual deterrent value versus a purely
   theoretical backstop?
4. **The scenario the paper doesn't model.** A bank or PAC with an
   information or communications edge (e.g., knowledge of a dovish
   Fed speech landing that afternoon, per the paper's own July 2025
   Waller/Bowman example on p.4) trades ahead of it on Kalshi to shape
   press narrative about "what markets expect." Distinguish this from
   illegal insider trading (trading on MNPI obtained improperly) vs. legal
   but narrative-shaping large directional bets — the policy risk is
   different for each.

## What to build in `notebooks/` to support this

A volume/open-interest comparison notebook: pull daily volume for every
series in Table 1 (not just fed funds rate) via `src/kalshi_api.py`, and
plot liquidity by series on a common scale. This single chart — "here's how
much thinner GDP and recession markets are than the FFR market the FEDS
paper focuses on" — is probably the single most persuasive piece of
original evidence this project can add.
