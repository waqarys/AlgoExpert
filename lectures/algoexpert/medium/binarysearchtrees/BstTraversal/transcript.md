# AlgoExpert · Bst Traversal

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Bst Traversal (0:00) — `slides/01.png`

Let's solve Bst Traversal, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. In-order, pre-order and post-order traversals appending into a list.

## 3. Intuition (0:19) — `slides/03.png`

In-order, pre-order and post-order differ only in when the node is visited relative to its children.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, in-order: left, node, right. Second, pre-order: node, left, right. Third, post-order: left, right, node.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with in order traverse. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:49) — `slides/07.png`

To recap Bst Traversal: In-order, pre-order and post-order differ only in when the node is visited relative to its children. Try re-implementing it from scratch without looking.
