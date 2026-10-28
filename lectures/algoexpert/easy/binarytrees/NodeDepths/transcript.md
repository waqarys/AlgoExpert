# AlgoExpert · Node Depths

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Node Depths (0:00) — `slides/01.png`

Let's solve Node Depths, an easy binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sum of the depths (distance from root) of every node.

## 3. Intuition (0:17) — `slides/03.png`

Each node contributes its depth, so pass the depth down while traversing and add it up.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

A naive approach finds each node's depth separately. Passing the depth down during one traversal gives linear time. A breadth-first version multiplies each level's size by its depth.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, traverse from the root at depth zero. Second, add the current depth to the total. Third, visit children with depth plus one. Fourth, return the sum.

## 6. Worked example (0:49) — `slides/06.png`

Node 1 sits at depth 0, so the running total becomes 0.

## 7. Worked example (0:54) — `slides/07.png`

Node 4 sits at depth 2, so the running total becomes 3.

## 8. Worked example (0:59) — `slides/08.png`

Node 9 sits at depth 3, so the running total becomes 9.

## 9. Worked example (1:04) — `slides/09.png`

Node 3 sits at depth 1, so the running total becomes 12.

## 10. Worked example (1:09) — `slides/10.png`

Node 7 sits at depth 2, so the running total becomes 16.

## 11. Java solution (1:14) — `slides/11.png`

The helper returns zero for a null node, otherwise the current depth plus the results for both children at depth plus one.

## 12. Complexity (1:22) — `slides/12.png`

Time is O of n. Space is O of h.

## 13. Edge cases & pitfalls (1:25) — `slides/13.png`

Remember the root has depth zero, and an empty tree sums to zero.

## 14. Interview tips & follow-ups (1:30) — `slides/14.png`

Mention the iterative version. The very hard follow-up, All Kinds of Node Depths, sums this value for every subtree.

## 15. Recap (1:39) — `slides/15.png`

To recap Node Depths: Each node contributes its depth, so pass the depth down while traversing and add it up. Try re-implementing it from scratch without looking.
