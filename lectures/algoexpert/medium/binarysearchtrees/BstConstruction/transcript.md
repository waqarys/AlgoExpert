# AlgoExpert · Bst Construction

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Bst Construction (0:00) — `slides/01.png`

Let's solve Bst Construction, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. A BST class supporting insert, contains and remove (duplicates go right; removing a node with two children replaces it with its in-order successor's value). Removing the only node is a no-op.

## 3. Intuition (0:26) — `slides/03.png`

Insert, search and remove all follow the BST ordering; removal of a two-child node swaps in the smallest value of the right subtree.

## 4. Approach (0:34) — `slides/04.png`

Step by step. First, walk left or right by comparison. Second, insert at the empty spot. Third, to remove with two children, copy the right subtree's minimum and delete it there. Fourth, handle the root carefully.

## 5. Java solution (1/2) (0:51) — `slides/05.png`

Here's the Java solution, starting with bst. It follows the steps we just described.

## 6. Java solution (2/2) (0:58) — `slides/06.png`

Continuing with remove, remove, min value.

## 7. Complexity (1:02) — `slides/07.png`

Time is O of log n avg, O of n worst per op. Space is constant (iterative).

## 8. Recap (1:08) — `slides/08.png`

To recap Bst Construction: Insert, search and remove all follow the BST ordering; removal of a two-child node swaps in the smallest value of the right subtree. Try re-implementing it from scratch without looking.
