# AlgoExpert · Product Sum

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Product Sum (0:00) — `slides/01.png`

Let's solve Product Sum, an easy recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. A "special" array holds ints or nested special arrays; each nested array's sum is multiplied by its depth (outermost equals 1).

## 3. Intuition (0:21) — `slides/03.png`

A nested array's sum is multiplied by its depth, which is naturally recursive.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, sum the elements at this level. Second, for a nested list, recurse with depth plus one. Third, multiply the level sum by the depth. Fourth, return it.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with product sum. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of n total elements. Space is O of d depth.

## 7. Recap (0:54) — `slides/07.png`

To recap Product Sum: A nested array's sum is multiplied by its depth, which is naturally recursive. Try re-implementing it from scratch without looking.
