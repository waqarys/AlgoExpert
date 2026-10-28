# AlgoExpert · Repair Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Repair Bst (0:00) — `slides/01.png`

Let's solve Repair Bst, a hard binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Exactly two nodes' values were swapped; swap them back in place. Iterative in-order finds the two out-of-order nodes.

## 3. Intuition (0:22) — `slides/03.png`

An in-order traversal of a BST is sorted; the two swapped nodes show up as order violations.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, in-order traverse tracking the previous node. Second, the first violation gives the first node. Third, the last violation gives the second. Fourth, swap their values.

## 5. Java solution (0:44) — `slides/05.png`

Here's the Java solution, starting with repair bst. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:55) — `slides/07.png`

To recap Repair Bst: An in-order traversal of a BST is sorted; the two swapped nodes show up as order violations. Try re-implementing it from scratch without looking.
