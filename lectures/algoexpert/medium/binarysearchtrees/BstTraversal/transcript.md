# AlgoExpert · Bst Traversal

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Bst Traversal (0:00) — `slides/01.png`

Let's solve Bst Traversal, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. In-order, pre-order and post-order traversals appending into a list.

## 3. Intuition (0:19) — `slides/03.png`

In-order, pre-order and post-order differ only in when the node is visited relative to its children.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

All three traversals visit every node once, linear time, with recursion depth equal to the height. The only difference is when we record the node relative to its children.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, in-order: left, node, right. Second, pre-order: node, left, right. Third, post-order: left, right, node.

## 6. Worked example (0:49) — `slides/06.png`

In-order, left, node, right: 1, 2, 5, 5, 10, 15, 22. Notice in-order gives sorted values.

## 7. Worked example (0:59) — `slides/07.png`

Pre-order, node, left, right: 10, 5, 2, 1, 5, 15, 22.

## 8. Worked example (1:06) — `slides/08.png`

Post-order, left, right, node: 1, 2, 5, 5, 22, 15, 10.

## 9. Java solution (1:13) — `slides/09.png`

Each method checks for null, then the only difference is the line that adds the value: between the recursive calls for in-order, before them for pre-order, and after them for post-order.

## 10. Complexity (1:23) — `slides/10.png`

Time is O of n. Space is O of n.

## 11. Edge cases & pitfalls (1:27) — `slides/11.png`

In-order traversal of a BST yields sorted values. Very deep trees can overflow the call stack, so know the iterative versions.

## 12. Interview tips & follow-ups (1:36) — `slides/12.png`

Pre-order is used to copy or serialise a tree; post-order to delete it or evaluate expressions. Morris traversal achieves constant space.

## 13. Recap (1:46) — `slides/13.png`

To recap Bst Traversal: In-order, pre-order and post-order differ only in when the node is visited relative to its children. Try re-implementing it from scratch without looking.
