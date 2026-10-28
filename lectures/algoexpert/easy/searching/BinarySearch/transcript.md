# AlgoExpert · Binary Search

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Binary Search (0:00) — `slides/01.png`

Let's solve Binary Search, an easy searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return the index of target in a sorted array, or -1.

## 3. Intuition (0:18) — `slides/03.png`

In a sorted array, comparing with the middle element tells us which half can contain the target.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, keep left and right bounds. Second, check the middle. Third, discard the half that can't contain the target. Fourth, return the index or minus one.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with binary search. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of log n. Space is constant.

## 7. Recap (0:49) — `slides/07.png`

To recap Binary Search: In a sorted array, comparing with the middle element tells us which half can contain the target. Try re-implementing it from scratch without looking.
