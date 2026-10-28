# AlgoExpert · Evaluate Expression Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Evaluate Expression Tree (0:00) — `slides/01.png`

Let's solve Evaluate Expression Tree, an easy binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Leaves are positive ints; internal nodes encode operators -1 ' plus ', -2 '-', -3 '/' (truncating), -4 ' '. Evaluate the tree.

## 3. Intuition (0:25) — `slides/03.png`

Leaves are numbers and internal nodes are operators, so evaluate the children first and combine them.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, if the node is a leaf, return its value. Second, evaluate left and right subtrees. Third, apply the operator encoded at the node. Fourth, division truncates toward zero.

## 5. Java solution (0:47) — `slides/05.png`

Here's the Java solution, starting with evaluate expression tree. It follows the steps we just described.

## 6. Complexity (0:55) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:59) — `slides/07.png`

To recap Evaluate Expression Tree: Leaves are numbers and internal nodes are operators, so evaluate the children first and combine them. Try re-implementing it from scratch without looking.
