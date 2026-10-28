# AlgoExpert · Validate Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Validate Bst (0:00) — `slides/01.png`

Let's solve Validate Bst, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Every node must be strictly greater than all left-subtree values and under equals all right-subtree values.

## 3. Intuition (0:20) — `slides/03.png`

Every node must lie within bounds inherited from its ancestors, not just compared with its parent.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

The tempting mistake is to compare each node only with its direct children, which misses violations deeper down. Either check that in-order traversal is sorted, or pass down bounds inherited from all ancestors, which lets us stop at the first violation.

## 5. Approach (0:41) — `slides/05.png`

Step by step. First, start with minus and plus infinity. Second, check the node is within bounds. Third, left child tightens the upper bound. Fourth, right child tightens the lower bound.

## 6. Worked example (0:57) — `slides/06.png`

Node 10 must be at least -∞ and less than ∞. It is, so we continue.

## 7. Worked example (1:04) — `slides/07.png`

Node 5 must be at least -∞ and less than 10. It is, so we continue.

## 8. Worked example (1:11) — `slides/08.png`

Node 15 must be at least 10 and less than ∞. It is, so we continue.

## 9. Worked example (1:18) — `slides/09.png`

Node 8 must be at least 10 and less than 15. It isn't: eight is in ten's right subtree, so the tree is not a valid BST.

## 10. Java solution (1:27) — `slides/10.png`

Valid returns true for null. It fails if the value is below the minimum or at least the maximum. Then it recurses left with the max tightened to the node's value, and right with the min raised to it.

## 11. Complexity (1:39) — `slides/11.png`

Time is O of n. Space is O of h.

## 12. Edge cases & pitfalls (1:43) — `slides/12.png`

The classic bug is a grandchild that's fine relative to its parent but violates an ancestor. Duplicates go right, and long bounds handle extreme integer values.

## 13. Interview tips & follow-ups (1:54) — `slides/13.png`

Draw a counterexample for the naive approach before coding. The hard follow-up repairs a BST with two swapped nodes.

## 14. Recap (2:02) — `slides/14.png`

To recap Validate Bst: Every node must lie within bounds inherited from its ancestors, not just compared with its parent. Try re-implementing it from scratch without looking.
