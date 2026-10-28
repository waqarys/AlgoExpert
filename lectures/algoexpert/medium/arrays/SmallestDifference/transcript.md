# AlgoExpert · Smallest Difference

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Smallest Difference (0:00) — `slides/01.png`

Let's solve Smallest Difference, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Pick one number from each array with the smallest absolute difference; return a, b .

## 3. Intuition (0:19) — `slides/03.png`

Sort both arrays, then walk them together, always advancing the smaller value to close the gap.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, sort both. Second, compare current values and record the gap. Third, advance the pointer at the smaller value. Fourth, stop early on zero.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with smallest difference. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n log n plus m log m. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Smallest Difference: Sort both arrays, then walk them together, always advancing the smaller value to close the gap. Try re-implementing it from scratch without looking.
