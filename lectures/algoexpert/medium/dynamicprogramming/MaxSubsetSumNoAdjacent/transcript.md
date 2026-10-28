# AlgoExpert · Max Subset Sum No Adjacent

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Max Subset Sum No Adjacent (0:00) — `slides/01.png`

Let's solve Max Subset Sum No Adjacent, a medium dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Max sum of positive ints with no two chosen elements adjacent.

## 3. Intuition (0:19) — `slides/03.png`

At each index, either take it plus the best up to two back, or skip it.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, keep the best up to i minus one and i minus two. Second, choose the max of skip or take. Third, slide forward.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with max subset sum no adjacent. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:48) — `slides/07.png`

To recap Max Subset Sum No Adjacent: At each index, either take it plus the best up to two back, or skip it. Try re-implementing it from scratch without looking.
