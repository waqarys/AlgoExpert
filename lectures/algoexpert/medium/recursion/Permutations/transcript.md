# AlgoExpert · Permutations

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Permutations (0:00) — `slides/01.png`

Let's solve Permutations, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. All orderings of a list of distinct ints (empty input yields an empty list).

## 3. Intuition (0:19) — `slides/03.png`

Build permutations by swapping each remaining element into the current position.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, recurse on index i. Second, swap each later element into position i. Third, recurse, then swap back.

## 5. Java solution (0:35) — `slides/05.png`

Here's the Java solution, starting with get permutations. It follows the steps we just described.

## 6. Complexity (0:42) — `slides/06.png`

Time is O of n times n factorial. Space is O of n times n factorial.

## 7. Recap (0:49) — `slides/07.png`

To recap Permutations: Build permutations by swapping each remaining element into the current position. Try re-implementing it from scratch without looking.
