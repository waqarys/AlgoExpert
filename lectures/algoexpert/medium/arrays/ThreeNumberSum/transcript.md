# AlgoExpert · Three Number Sum

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Three Number Sum (0:00) — `slides/01.png`

Let's solve Three Number Sum, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. All triplets of distinct integers summing to target, each triplet ascending and the list sorted. Sort then sweep with two pointers.

## 3. Intuition (0:21) — `slides/03.png`

Fix one number, then find pairs in the sorted remainder with two pointers.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, sort the array. Second, for each index, set left and right pointers after it. Third, move them based on the current sum. Fourth, record exact matches.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with three number sum. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n squared. Space is O of n.

## 7. Recap (0:54) — `slides/07.png`

To recap Three Number Sum: Fix one number, then find pairs in the sorted remainder with two pointers. Try re-implementing it from scratch without looking.
