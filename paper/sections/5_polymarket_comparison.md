# 5. Regulated vs. Unregulated Signal Quality: Kalshi vs. Polymarket

*Status: new section — the FEDS paper only compares Kalshi to itself and to
traditional instruments (surveys, futures, options). It mentions Polymarket
once to dismiss it.*

## What the FEDS paper says about Polymarket (verbatim framing, p.8)

"Other platforms offering prediction markets include Polymarket, PredictIt,
and Interactive Brokers. Of these, only Kalshi and Interactive Brokers
operate under regulatory approval. Polymarket operates in a legal gray
area and, along with PredictIt and Interactive Brokers, supports fewer
contracts, lower liquidity, and smaller individual position limits."

The FEDS paper also cites, without engaging directly, **Eichengreen,
Viswanath-Natraj, Wang and Wang (2025)**, who use Polymarket data to study
questions around Fed independence (p.7, "Related Literature").

## What this section should do that the FEDS paper doesn't

1. **Identify Polymarket's Fed/macro contracts contemporaneous with the
   Kalshi series the FEDS paper studies** (FOMC rate decisions at minimum;
   Polymarket may not have direct analogs for CPI/GDP/unemployment — verify
   what actually exists rather than assuming symmetry).
2. **Run the same pipeline on both.** Apply the FEDS paper's own
   strike-ladder-to-pdf method (or Polymarket's equivalent binary-contract
   structure) to extract comparable mean/median/mode forecasts, and
   replicate the Figure-1-style forecast-error-by-days-before-FOMC chart
   for Polymarket alongside Kalshi.
3. **Test the "regulation improves signal quality" hypothesis directly**,
   rather than asserting it. Candidate metrics:
   - Forecast error (MAE/RMSE) — does Kalshi actually forecast better, or
     just have more contracts and cleaner data availability?
   - Bid-ask spread / price staleness — does CFTC market-maker
     infrastructure (Susquehanna, per the FEDS paper) produce tighter
     markets than Polymarket's largely automated-market-maker or
     peer-to-peer liquidity?
   - Divergence around known-controversial events (e.g., a Fed independence
     question, per Eichengreen et al.) — does Polymarket's pseudonymous,
     crypto-native user base produce systematically different tail pricing
     than Kalshi's KYC'd, regulated, partly-institutional user base?
4. **Note the confound honestly.** Kalshi and Polymarket don't just differ
   in regulatory status — they differ in user base composition, contract
   design, settlement currency (USD vs. USDC), and history. A clean
   "regulated vs. unregulated" causal claim is hard to support from
   observational data; frame results as suggestive, not causal, unless the
   evidence is unusually strong.

## Deliverable for this section

A side-by-side version of the FEDS paper's Figure 1 (or Table 3) with a
Polymarket series added, plus 2–3 paragraphs on what the comparison does
and doesn't tell you about whether CFTC regulation is doing real work for
signal quality versus just being a legal/legitimacy label.
