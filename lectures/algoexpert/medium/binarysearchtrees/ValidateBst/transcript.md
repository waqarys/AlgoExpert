# AlgoExpert · Validate Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Validate Bst (0:00) — `slides/01.png`

Let's solve Validate Bst, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Every node must be strictly greater than all left-subtree values and under equals all right-subtree values.

## 3. Intuition (0:20) — `slides/03.png`

Every node must lie within bounds inherited from its ancestors, not just compared with its parent.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, start with minus and plus infinity. Second, check the node is within bounds. Third, left child tightens the upper bound. Fourth, right child tightens the lower bound.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with validate bst. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:53) — `slides/07.png`

To recap Validate Bst: Every node must lie within bounds inherited from its ancestors, not just compared with its parent. Try re-implementing it from scratch without looking.
