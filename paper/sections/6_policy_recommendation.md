# 6. Policy Recommendation

*Status: new section, and the actual differentiator of this project. The
FEDS paper stops at "this is an accurate forecasting tool." This section
should not stop there.*

## Working thesis to develop and defend

> A Kalshi-based distributional dashboard should **supplement, not
> replace**, existing Fed expectations tools (SME, Bloomberg consensus,
> SPF, fed funds futures), and should only be cited in official
> communications or publications once three safeguards are in place.

## Draft safeguards (refine with evidence from Sections 3–5 before finalizing)

1. **A minimum liquidity/volume floor before a series is citable.**
   Grounded in Section 3's thin-market findings: the FFR series (hundreds
   of millions in volume, per the FEDS paper's own Figure 3) is a very
   different animal from a GDP or recession-probability series with a
   two-to-four-year listing history. Propose a concrete threshold (e.g.,
   minimum open interest or trailing 7-day volume) below which a contract's
   price should not be treated as a citable expectations measure — modeled
   loosely on how the Fed already treats sparse or thin financial-market
   data with caution.
2. **Position-concentration monitoring in the pre-FOMC window**, leveraging
   Kalshi's existing CFTC large-trader reporting obligations as a DCM.
   Concretely: flag (internally, not necessarily publicly) any FOMC-week
   price move attributable to a small number of large accounts before that
   move is treated as informative "market expectations" rather than one
   trader's bet.
3. **Distributional framing, not point-estimate framing, with an explicit
   disclaimer.** Present mean/median/mode/variance/skew together (as the
   FEDS paper's own methodology naturally supports) rather than a single
   headline number, and label it clearly as a retail-market-derived
   measure — "what traders are pricing," not "what the Fed expects" —
   preserving the separation the Fed currently maintains between
   market-implied and staff/SEP-based projections. This directly answers
   the optics question in Section 4/5: officials can reference it the way
   they already reference fed funds futures probabilities, without implying
   endorsement of betting markets as a policy input.

## Recommended concrete format

Propose a specific, minimal first step rather than a sweeping one — e.g.:
a quarterly appendix chart in the Monetary Policy Report, or a NY Fed
markets-desk-style public webpage (paralleling how SOFR/repo data is
published), sourced explicitly to Kalshi with the three safeguards above
noted alongside it. This is deliberately more conservative than "cite it in
FOMC statements" — justify why, using the legitimacy/optics analysis from
whichever framing Section 4/5 land on.

## What this section must NOT do

Don't hedge into "more research is needed" as the final word — that's the
default academic ending the FEDS paper itself effectively takes ("our goal
is to facilitate further research," p.4). The whole point of this project
is to go one step further and commit to a specific, falsifiable
recommendation, even a modest one.
