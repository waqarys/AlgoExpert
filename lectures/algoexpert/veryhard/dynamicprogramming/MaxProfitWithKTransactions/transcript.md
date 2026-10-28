# AlgoExpert · Max Profit With K Transactions

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Max Profit With K Transactions (0:00) — `slides/01.png`

Let's solve Max Profit With K Transactions, a very hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:13) — `slides/02.png`

Here's the problem. Daily prices, at most k buy or sell pairs (no overlap); max profit.

## 3. Intuition (0:20) — `slides/03.png`

For each transaction count, track the best profit by day using the best buy so far.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, rows for transactions, columns for days. Second, carry max of previous row minus price. Third, profit is max of skip or sell today. Fourth, two rows suffice.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with max profit with k transactions. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n times k. Space is O of n.

## 7. Recap (0:54) — `slides/07.png`

To recap Max Profit With K Transactions: For each transaction count, track the best profit by day using the best buy so far. Try re-implementing it from scratch without looking.
