# AlgoExpert · Knapsack Problem

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Knapsack Problem (0:00) — `slides/01.png`

Let's solve Knapsack Problem, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Items are value, weight . Returns maxValue , item indices .

## 3. Intuition (0:20) — `slides/03.png`

Each item is taken or skipped; a table over items and capacities captures every choice.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, row per item, column per capacity. Second, skip copies the row above. Third, take adds the value to the row above at capacity minus weight. Fourth, backtrack to list items.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with knapsack problem. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n times c. Space is O of n times c.

## 7. Recap (0:54) — `slides/07.png`

To recap Knapsack Problem: Each item is taken or skipped; a table over items and capacities captures every choice. Try re-implementing it from scratch without looking.
