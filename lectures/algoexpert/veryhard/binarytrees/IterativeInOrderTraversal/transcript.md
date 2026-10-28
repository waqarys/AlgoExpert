# AlgoExpert · Iterative In Order Traversal

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Iterative In Order Traversal (0:00) — `slides/01.png`

Let's solve Iterative In Order Traversal, a very hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. In-order traversal with constant extra space using parent pointers.

## 3. Intuition (0:19) — `slides/03.png`

Parent pointers let us know where we came from, so we can walk without a stack.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Recursion and explicit stacks both use height space. With parent pointers, tracking the previous node is enough for constant space.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, track previous and current. Second, coming from parent, go left if possible. Third, coming from left, visit then go right. Fourth, coming from right, go up.

## 6. Worked example (0:49) — `slides/06.png`

With parent pointers, we can traverse in-order using only prev and current.

## 7. Worked example (0:54) — `slides/07.png`

If we came from the parent, go left if we can, else visit and go right or up. From the left child, visit and go right or up. From the right child, go up.

## 8. Worked example (1:06) — `slides/08.png`

That yields the in-order sequence four, two, one, six, three, seven.

## 9. Java solution (1:12) — `slides/09.png`

We loop while current exists, choose next by the three cases, calling the callback at the right moments, then shift prev and current.

## 10. Complexity (1:20) — `slides/10.png`

Time is O of n. Space is constant.

## 11. Edge cases & pitfalls (1:24) — `slides/11.png`

Carefully distinguish arriving from the left child versus the right.

## 12. Interview tips & follow-ups (1:28) — `slides/12.png`

Morris traversal does constant space without parent pointers.

## 13. Recap (1:33) — `slides/13.png`

To recap Iterative In Order Traversal: Parent pointers let us know where we came from, so we can walk without a stack. Try re-implementing it from scratch without looking.
