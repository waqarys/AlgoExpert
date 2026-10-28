# AlgoExpert · Next Greater Element

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Next Greater Element (0:00) — `slides/01.png`

Let's solve Next Greater Element, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. For each element of a circular array, the next strictly greater value, or -1.

## 3. Intuition (0:19) — `slides/03.png`

A monotonic stack holds indices still waiting for a greater value; loop twice for circularity.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Scanning forward from every element is quadratic. A decreasing stack of unresolved indices resolves them as soon as a bigger value appears. Looping twice handles the circular wrap.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, iterate twice around the array. Second, pop indices whose value is smaller and assign the answer. Third, push the current index.

## 6. Worked example (0:51) — `slides/06.png`

2 is greater than nothing waiting; push it.

## 7. Worked example (0:55) — `slides/07.png`

5 is greater than 2 on the stack, so it's their answer.

## 8. Worked example (0:59) — `slides/08.png`

6 is greater than -4, -3, 5 on the stack, so it's their answer.

## 9. Worked example (1:05) — `slides/09.png`

7 is greater than 6 on the stack, so it's their answer.

## 10. Worked example (1:10) — `slides/10.png`

In the second pass, 5 is greater than 2 on the stack, so it's their answer.

## 11. Java solution (1:15) — `slides/11.png`

We fill the output with minus one and loop i to two n, using j equal i mod n. While the top's value is smaller than a of j, pop and set its answer. Push j only in the first pass.

## 12. Complexity (1:28) — `slides/12.png`

Time is O of n. Space is O of n.

## 13. Edge cases & pitfalls (1:31) — `slides/13.png`

Store indices so you can write the answer. Only push during the first pass.

## 14. Interview tips & follow-ups (1:38) — `slides/14.png`

The same pattern solves daily temperatures and stock span.

## 15. Recap (1:42) — `slides/15.png`

To recap Next Greater Element: A monotonic stack holds indices still waiting for a greater value; loop twice for circularity. Try re-implementing it from scratch without looking.
