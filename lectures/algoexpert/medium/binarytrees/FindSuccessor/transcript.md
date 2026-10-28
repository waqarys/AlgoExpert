# AlgoExpert · Find Successor

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Successor (0:00) — `slides/01.png`

Let's solve Find Successor, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Nodes have parent pointers; return the in-order successor of node (or null).

## 3. Intuition (0:19) — `slides/03.png`

The in-order successor is the leftmost node of the right subtree, or else the first ancestor reached from a left child.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, if there's a right subtree, go right then all the way left. Second, otherwise climb parents until we come from a left child.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with find successor. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of h. Space is constant.

## 7. Recap (0:48) — `slides/07.png`

To recap Find Successor: The in-order successor is the leftmost node of the right subtree, or else the first ancestor reached from a left child. Try re-implementing it from scratch without looking.
