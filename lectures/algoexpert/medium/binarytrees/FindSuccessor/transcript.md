# AlgoExpert · Find Successor

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Successor (0:00) — `slides/01.png`

Let's solve Find Successor, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Nodes have parent pointers; return the in-order successor of node (or null).

## 3. Intuition (0:19) — `slides/03.png`

The in-order successor is the leftmost node of the right subtree, or else the first ancestor reached from a left child.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

The simple approach does a full in-order traversal and returns the next element, linear time and space. With parent pointers, we only need two cases, costing at most the tree's height and constant space.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, if there's a right subtree, go right then all the way left. Second, otherwise climb parents until we come from a left child.

## 6. Worked example (0:49) — `slides/06.png`

Find the in-order successor of five. Five has no right child, so the successor is above it.

## 7. Worked example (0:57) — `slides/07.png`

Five is its parent two's right child, so two comes before it. Keep climbing.

## 8. Worked example (1:03) — `slides/08.png`

Two is the left child of one, so one is the successor.

## 9. Worked example (1:07) — `slides/09.png`

For node one, which has a right subtree, the successor is the leftmost node of that subtree: three.

## 10. Java solution (1:14) — `slides/10.png`

If the node has a right child, we go right once and then all the way left. Otherwise we climb while the current node is its parent's right child and return the parent, which is null if we ran off the top.

## 11. Complexity (1:26) — `slides/11.png`

Time is O of h. Space is constant.

## 12. Edge cases & pitfalls (1:29) — `slides/12.png`

The last node in order has no successor, so return null. Climb only while the current node is its parent's right child.

## 13. Interview tips & follow-ups (1:37) — `slides/13.png`

The predecessor is the mirror image. In a BST without parent pointers, search from the root tracking the last left turn.

## 14. Recap (1:46) — `slides/14.png`

To recap Find Successor: The in-order successor is the leftmost node of the right subtree, or else the first ancestor reached from a left child. Try re-implementing it from scratch without looking.
