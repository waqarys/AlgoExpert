# AlgoExpert · Juice Bottling

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Juice Bottling (0:00) — `slides/01.png`

Let's solve Juice Bottling, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Prices i is the price of a bottle of size i (prices 0 equals 0). Split the total (prices.length - 1 units) into bottle sizes maximising revenue; return sizes (rod cutting).

## 3. Intuition (0:26) — `slides/03.png`

Unbounded knapsack over sizes: best price for each total is a bottle plus the best for the remainder.

## 4. Approach (0:33) — `slides/04.png`

Step by step. First, best of zero is zero. Second, for each size, try every first bottle. Third, store the best choice. Fourth, rebuild the bottle sizes.

## 5. Java solution (0:47) — `slides/05.png`

Here's the Java solution, starting with juice bottling. It follows the steps we just described.

## 6. Complexity (0:54) — `slides/06.png`

Time is O of n squared. Space is O of n.

## 7. Recap (0:59) — `slides/07.png`

To recap Juice Bottling: Unbounded knapsack over sizes: best price for each total is a bottle plus the best for the remainder. Try re-implementing it from scratch without looking.
