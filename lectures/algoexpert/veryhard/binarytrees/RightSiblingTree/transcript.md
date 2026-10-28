# AlgoExpert · Right Sibling Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Right Sibling Tree (0:00) — `slides/01.png`

Let's solve Right Sibling Tree, a very hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Transform in place so every node's right pointer points to the next node on the same level (null at the end of a level); left pointers keep the first child. Level-by-level, constant extra space using the already-linked level above.

## 3. Intuition (0:27) — `slides/03.png`

Process top-down: a left child's sibling is the right child, and a right child's sibling is the parent's sibling's left child.

## 4. Brute force vs optimal (0:34) — `slides/04.png`

Level-order processing is straightforward and linear. The recursive version uses the parent's new sibling pointer to reach cousins, saving space.

## 5. Approach (0:44) — `slides/05.png`

Step by step. First, recurse with parent and side. Second, save the old right child. Third, set right to the sibling. Fourth, recurse on children.

## 6. Worked example (0:57) — `slides/06.png`

Rewire every node so its right pointer points to the next node on the same level.

## 7. Worked example (1:02) — `slides/07.png`

Gather each level's nodes first, from the old pointers, then rewire right pointers along the level.

## 8. Worked example (1:09) — `slides/08.png`

Collecting the next level before overwriting right pointers is what keeps the right children reachable.

## 9. Java solution (1:15) — `slides/09.png`

We build each next level from the current level's children, then set each node's right to the following node in the level.

## 10. Complexity (1:22) — `slides/10.png`

Time is O of n. Space is constant (iterative, besides an original-children snapshot per level).

## 11. Edge cases & pitfalls (1:28) — `slides/11.png`

Grab the children before you overwrite right.

## 12. Interview tips & follow-ups (1:32) — `slides/12.png`

Mention the recursive variant.

## 13. Recap (1:35) — `slides/13.png`

To recap Right Sibling Tree: Process top-down: a left child's sibling is the right child, and a right child's sibling is the parent's sibling's left child. Try re-implementing it from scratch without looking.
