# AlgoExpert · Branch Sums

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Branch Sums (0:00) — `slides/01.png`

Let's solve Branch Sums, an easy binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. List the root-to-leaf path sums, ordered left to right.

## 3. Intuition (0:17) — `slides/03.png`

Carry the running sum down each path; at a leaf, that sum is one branch sum.

## 4. Brute force vs optimal (0:22) — `slides/04.png`

A naive approach stores each full path and sums it at the leaf, repeating work for shared prefixes. Instead we pass the running sum down the recursion, so each node is added exactly once.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, depth-first from the root with sum zero. Second, add the node's value. Third, at a leaf, record the sum. Fourth, recurse left then right to keep left-to-right order.

## 6. Worked example (0:49) — `slides/06.png`

Reaching leaf 8, the running total along this path is 15, so we record it.

## 7. Worked example (0:55) — `slides/07.png`

Reaching leaf 9, the running total along this path is 16, so we record it.

## 8. Worked example (1:00) — `slides/08.png`

Reaching leaf 10, the running total along this path is 18, so we record it.

## 9. Worked example (1:06) — `slides/09.png`

Reaching leaf 6, the running total along this path is 10, so we record it.

## 10. Worked example (1:11) — `slides/10.png`

Reaching leaf 7, the running total along this path is 11, so we record it.

## 11. Java solution (1:17) — `slides/11.png`

The helper takes a node, the running sum and the result list. It adds the node's value, records the sum at a leaf, and otherwise recurses left then right.

## 12. Complexity (1:27) — `slides/12.png`

Time is O of n. Space is O of n.

## 13. Edge cases & pitfalls (1:31) — `slides/13.png`

The common bug is treating a node with one child as a leaf. A node is a leaf only when both children are null.

## 14. Interview tips & follow-ups (1:39) — `slides/14.png`

Follow-ups include returning the paths, or checking whether any path sums to a target. You can also do it iteratively with a stack of node and sum pairs.

## 15. Recap (1:49) — `slides/15.png`

To recap Branch Sums: Carry the running sum down each path; at a leaf, that sum is one branch sum. Try re-implementing it from scratch without looking.
