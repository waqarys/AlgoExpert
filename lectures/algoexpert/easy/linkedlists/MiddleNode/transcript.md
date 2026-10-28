# AlgoExpert · Middle Node

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Middle Node (0:00) — `slides/01.png`

Let's solve Middle Node, an easy linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return the middle node (second middle for even lengths) via slow or fast pointers.

## 3. Intuition (0:19) — `slides/03.png`

A fast pointer moving two steps lands at the end exactly when a slow pointer moving one step reaches the middle.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, start slow and fast at the head. Second, advance slow by one, fast by two. Third, stop when fast runs out. Fourth, return slow.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with middle node. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:50) — `slides/07.png`

To recap Middle Node: A fast pointer moving two steps lands at the end exactly when a slow pointer moving one step reaches the middle. Try re-implementing it from scratch without looking.
