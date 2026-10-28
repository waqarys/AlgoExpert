# AlgoExpert · Water Area

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Water Area (0:00) — `slides/01.png`

Let's solve Water Area, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Pillars of given heights; how much rain water is trapped? Two pointers.

## 3. Intuition (0:19) — `slides/03.png`

Water above a pillar is limited by the smaller of the tallest walls on its left and right.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, pointers at both ends with running maxes. Second, move the side with the smaller max. Third, add max minus height. Fourth, continue until they meet.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with water area. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:49) — `slides/07.png`

To recap Water Area: Water above a pillar is limited by the smaller of the tallest walls on its left and right. Try re-implementing it from scratch without looking.
