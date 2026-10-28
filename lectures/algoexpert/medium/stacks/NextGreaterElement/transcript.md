# AlgoExpert · Next Greater Element

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Next Greater Element (0:00) — `slides/01.png`

Let's solve Next Greater Element, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. For each element of a circular array, the next strictly greater value, or -1.

## 3. Intuition (0:19) — `slides/03.png`

A monotonic stack holds indices still waiting for a greater value; loop twice for circularity.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, iterate twice around the array. Second, pop indices whose value is smaller and assign the answer. Third, push the current index.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with next greater element. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:50) — `slides/07.png`

To recap Next Greater Element: A monotonic stack holds indices still waiting for a greater value; loop twice for circularity. Try re-implementing it from scratch without looking.
