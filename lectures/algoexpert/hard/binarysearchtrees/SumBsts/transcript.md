# AlgoExpert · Sum Bsts

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sum Bsts (0:00) — `slides/01.png`

Let's solve Sum Bsts, a hard binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sum the values of every node that roots a valid BST subtree containing at least 3 nodes. Post-order collecting (isBst, size, min, max, sum).

## 3. Intuition (0:24) — `slides/03.png`

Post-order lets each node know whether both children are BSTs, their sizes, sums and value ranges.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Validating each subtree separately is quadratic. One post-order pass that returns validity, size, min, max and sum lets every node decide in constant time.

## 5. Approach (0:42) — `slides/05.png`

Step by step. First, return validity, size, sum, min and max from each subtree. Second, combine at the parent. Third, add sums of valid BSTs with three or more nodes.

## 6. Worked example (0:56) — `slides/06.png`

Each node returns whether its subtree is a BST, its size, min, max and sum, computed from its children.

## 7. Worked example (1:03) — `slides/07.png`

The subtree rooted at seven, with six and nine, is a BST with three nodes, sum twenty-two.

## 8. Worked example (1:10) — `slides/08.png`

At five, the left max is three and the right min is six, so it's a BST of five nodes summing to thirty. That replaces the twenty-two we counted inside it.

## 9. Worked example (1:20) — `slides/09.png`

Two has a right child of one, which breaks the BST rule, so the root fails too. The answer is thirty.

## 10. Java solution (1:28) — `slides/10.png`

Info recurses on both children, decides BST status from their max and min, and when the subtree is a BST of size three or more adds its sum, subtracting children already counted. It returns the tuple.

## 11. Complexity (1:41) — `slides/11.png`

Time is O of n. Space is O of h.

## 12. Edge cases & pitfalls (1:44) — `slides/12.png`

Only subtrees with at least three nodes count, and a larger valid BST replaces the contributions of the smaller ones inside it.

## 13. Interview tips & follow-ups (1:52) — `slides/13.png`

State the tuple you return from each call clearly; it's the whole trick.

## 14. Recap (1:57) — `slides/14.png`

To recap Sum Bsts: Post-order lets each node know whether both children are BSTs, their sizes, sums and value ranges. Try re-implementing it from scratch without looking.
