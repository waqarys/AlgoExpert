# AlgoExpert · Juice Bottling

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Juice Bottling (0:00) — `slides/01.png`

Let's solve Juice Bottling, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Prices i is the price of a bottle of size i (prices 0 equals 0). Split the total (prices.length - 1 units) into bottle sizes maximising revenue; return sizes (rod cutting).

## 3. Intuition (0:26) — `slides/03.png`

Unbounded knapsack over sizes: best price for each total is a bottle plus the best for the remainder.

## 4. Brute force vs optimal (0:33) — `slides/04.png`

Trying every partition is exponential. This is rod cutting: best of s is the max over first bottle k of price k plus best of s minus k, quadratic.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, best of zero is zero. Second, for each size, try every first bottle. Third, store the best choice. Fourth, rebuild the bottle sizes.

## 6. Worked example (0:58) — `slides/06.png`

For 1 units, try every first bottle size. The best is 1, starting with a bottle of 1.

## 7. Worked example (1:05) — `slides/07.png`

For 2 units, try every first bottle size. The best is 3, starting with a bottle of 2.

## 8. Worked example (1:13) — `slides/08.png`

For 3 units, try every first bottle size. The best is 4, starting with a bottle of 1.

## 9. Worked example (1:20) — `slides/09.png`

Following the cuts gives bottles of [1, 2], revenue 4.

## 10. Java solution (1:25) — `slides/10.png`

For each amount s and each first size k, update best and cut. Then walk down from n minus one subtracting cuts.

## 11. Complexity (1:34) — `slides/11.png`

Time is O of n squared. Space is O of n.

## 12. Edge cases & pitfalls (1:39) — `slides/12.png`

Price zero is always zero. Store the first cut so you can rebuild.

## 13. Interview tips & follow-ups (1:45) — `slides/13.png`

Name it the rod-cutting problem.

## 14. Recap (1:48) — `slides/14.png`

To recap Juice Bottling: Unbounded knapsack over sizes: best price for each total is a bottle plus the best for the remainder. Try re-implementing it from scratch without looking.
