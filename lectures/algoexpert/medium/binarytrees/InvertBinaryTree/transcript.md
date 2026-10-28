# AlgoExpert · Invert Binary Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Invert Binary Tree (0:00) — `slides/01.png`

Let's solve Invert Binary Tree, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Mirror the tree by swapping every node's children.

## 3. Intuition (0:17) — `slides/03.png`

Swap every node's children, recursively or with a queue.

## 4. Brute force vs optimal (0:22) — `slides/04.png`

Every node's children must be swapped, so linear time is optimal. Recursion uses stack space proportional to height; a breadth-first queue uses space proportional to the widest level. Order doesn't matter.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, visit each node. Second, swap left and right. Third, recurse into both children.

## 6. Worked example (0:46) — `slides/06.png`

Here's the original tree.

## 7. Worked example (0:49) — `slides/07.png`

At node 1, swap its left and right children.

## 8. Worked example (0:53) — `slides/08.png`

At node 2, swap its left and right children.

## 9. Worked example (0:57) — `slides/09.png`

At node 3, swap its left and right children.

## 10. Java solution (1:01) — `slides/10.png`

If the node is null, return. Otherwise swap left and right with a temporary, then invert both subtrees.

## 11. Complexity (1:09) — `slides/11.png`

Time is O of n. Space is O of h.

## 12. Edge cases & pitfalls (1:13) — `slides/12.png`

Swapping a null child is fine. For very deep trees, prefer the iterative version.

## 13. Interview tips & follow-ups (1:20) — `slides/13.png`

Mention the iterative version, and relate it to checking whether two trees are mirrors.

## 14. Recap (1:25) — `slides/14.png`

To recap Invert Binary Tree: Swap every node's children, recursively or with a queue. Try re-implementing it from scratch without looking.
