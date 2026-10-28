# AlgoExpert · Middle Node

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Middle Node (0:00) — `slides/01.png`

Let's solve Middle Node, an easy linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return the middle node (second middle for even lengths) via slow or fast pointers.

## 3. Intuition (0:19) — `slides/03.png`

A fast pointer moving two steps lands at the end exactly when a slow pointer moving one step reaches the middle.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

You could count the length and then walk half of it, which takes two passes, or copy the nodes into an array. The slow and fast pointer trick finds the middle in one pass with constant space.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, start slow and fast at the head. Second, advance slow by one, fast by two. Third, stop when fast runs out. Fourth, return slow.

## 6. Worked example (0:50) — `slides/06.png`

Both pointers start at the head, the node with value two.

## 7. Worked example (0:55) — `slides/07.png`

Slow moves one step to 7; fast moves two steps to 3.

## 8. Worked example (0:59) — `slides/08.png`

Slow moves one step to 3; fast moves two steps to 9.

## 9. Worked example (1:04) — `slides/09.png`

Fast is at the last node, so slow is at the middle: 3.

## 10. Java solution (1:09) — `slides/10.png`

Slow and fast start at the head. While fast and fast dot next aren't null, slow moves one step and fast moves two. Return slow.

## 11. Complexity (1:19) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:23) — `slides/12.png`

For an even length, the problem wants the second middle node, which this loop naturally returns. Always check fast and fast dot next before jumping.

## 13. Interview tips & follow-ups (1:33) — `slides/13.png`

The same pattern powers cycle detection and splitting a list in half for merge sort.

## 14. Recap (1:38) — `slides/14.png`

To recap Middle Node: A fast pointer moving two steps lands at the end exactly when a slow pointer moving one step reaches the middle. Try re-implementing it from scratch without looking.
