# AlgoExpert · Max Profit With K Transactions

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Max Profit With K Transactions (0:00) — `slides/01.png`

Let's solve Max Profit With K Transactions, a very hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:13) — `slides/02.png`

Here's the problem. Daily prices, at most k buy or sell pairs (no overlap); max profit.

## 3. Intuition (0:20) — `slides/03.png`

For each transaction count, track the best profit by day using the best buy so far.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

The naive DP checks every buy day for every sell day. Tracking the best value of previous profit minus price makes each row linear.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, rows for transactions, columns for days. Second, carry max of previous row minus price. Third, profit is max of skip or sell today. Fourth, two rows suffice.

## 6. Worked example (0:51) — `slides/06.png`

Prices five, eleven, three, fifty, sixty, ninety; at most two transactions.

## 7. Worked example (0:57) — `slides/07.png`

Row 1: the best profit by each day using at most 1 transactions. By the last day it's 87.

## 8. Worked example (1:05) — `slides/08.png`

Row 2: the best profit by each day using at most 2 transactions. By the last day it's 93.

## 9. Java solution (1:13) — `slides/09.png`

For each transaction count, we sweep days, updating best buy with prev profit minus price, and cur as the max of yesterday or selling today. Then swap rows.

## 10. Complexity (1:23) — `slides/10.png`

Time is O of n times k. Space is O of n.

## 11. Edge cases & pitfalls (1:27) — `slides/11.png`

If k is at least half the days, it's the unlimited case.

## 12. Interview tips & follow-ups (1:32) — `slides/12.png`

Explain best buy as the max of prior profit minus price.

## 13. Recap (1:37) — `slides/13.png`

To recap Max Profit With K Transactions: For each transaction count, track the best profit by day using the best buy so far. Try re-implementing it from scratch without looking.
