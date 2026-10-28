# AlgoExpert · Shifted Binary Search

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Shifted Binary Search (0:00) — `slides/01.png`

Let's solve Shifted Binary Search, a hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Find target's index in a sorted array of distinct ints rotated by some amount; -1 if absent.

## 3. Intuition (0:20) — `slides/03.png`

In a rotated sorted array, one half is always sorted; check if the target lies in it.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, find the middle. Second, decide which half is sorted. Third, check whether the target is in that half. Fourth, recurse into the right half.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with shifted binary search. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of log n. Space is constant.

## 7. Recap (0:52) — `slides/07.png`

To recap Shifted Binary Search: In a rotated sorted array, one half is always sorted; check if the target lies in it. Try re-implementing it from scratch without looking.
