# AlgoExpert · Min Number Of Coins For Change

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Number Of Coins For Change (0:00) — `slides/01.png`

Let's solve Min Number Of Coins For Change, a medium dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Fewest coins summing to n, or -1 if impossible.

## 3. Intuition (0:19) — `slides/03.png`

Build the fewest coins for every amount from zero up to n.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, array of infinities, zero for amount zero. Second, for each coin, relax amounts from the coin up. Third, answer or minus one.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with min number of coins for change. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n times d. Space is O of n.

## 7. Recap (0:48) — `slides/07.png`

To recap Min Number Of Coins For Change: Build the fewest coins for every amount from zero up to n. Try re-implementing it from scratch without looking.
