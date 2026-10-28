# AlgoExpert · Iterative In Order Traversal

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Iterative In Order Traversal (0:00) — `slides/01.png`

Let's solve Iterative In Order Traversal, a very hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. In-order traversal with constant extra space using parent pointers.

## 3. Intuition (0:19) — `slides/03.png`

Parent pointers let us know where we came from, so we can walk without a stack.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, track previous and current. Second, coming from parent, go left if possible. Third, coming from left, visit then go right. Fourth, coming from right, go up.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with iterative in order traversal. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Iterative In Order Traversal: Parent pointers let us know where we came from, so we can walk without a stack. Try re-implementing it from scratch without looking.
