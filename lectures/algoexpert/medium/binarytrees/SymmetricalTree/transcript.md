# AlgoExpert · Symmetrical Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Symmetrical Tree (0:00) — `slides/01.png`

Let's solve Symmetrical Tree, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Is the tree a mirror image of itself around its root?

## 3. Intuition (0:17) — `slides/03.png`

A tree is symmetric if the left subtree mirrors the right.

## 4. Brute force vs optimal (0:22) — `slides/04.png`

You could build a mirrored copy and compare, using extra memory. Better is checking pairs directly: the left subtree's outer child pairs with the right subtree's outer child, and inner with inner.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, compare two nodes at a time. Second, values must match. Third, outer children pair together and inner children pair together.

## 6. Worked example (0:45) — `slides/06.png`

Compare the mirrored pair: 2 on the left with 2 on the right. They match, so continue with outer and inner children.

## 7. Worked example (0:53) — `slides/07.png`

Compare the mirrored pair: 3 on the left with 3 on the right. They match, so continue with outer and inner children.

## 8. Worked example (1:01) — `slides/08.png`

Compare the mirrored pair: 4 on the left with 4 on the right. They match, so continue with outer and inner children.

## 9. Worked example (1:09) — `slides/09.png`

Compare the mirrored pair: 5 on the left with 5 on the right. They match, so continue with outer and inner children.

## 10. Java solution (1:18) — `slides/10.png`

Mirror returns true if both nodes are null and false if just one is. Otherwise values must be equal, and we recursively compare left's left with right's right, and left's right with right's left.

## 11. Complexity (1:29) — `slides/11.png`

Time is O of n. Space is O of h.

## 12. Edge cases & pitfalls (1:33) — `slides/12.png`

If one side is null and the other isn't, return false. Both structure and values must mirror.

## 13. Interview tips & follow-ups (1:40) — `slides/13.png`

An iterative version uses a queue of node pairs. Note that a tree is symmetric when it equals its own inversion.

## 14. Recap (1:48) — `slides/14.png`

To recap Symmetrical Tree: A tree is symmetric if the left subtree mirrors the right. Try re-implementing it from scratch without looking.
