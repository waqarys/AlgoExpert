# AlgoExpert · Right Sibling Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Right Sibling Tree (0:00) — `slides/01.png`

Let's solve Right Sibling Tree, a very hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Transform in place so every node's right pointer points to the next node on the same level (null at the end of a level); left pointers keep the first child. Level-by-level, constant extra space using the already-linked level above.

## 3. Intuition (0:27) — `slides/03.png`

Process top-down: a left child's sibling is the right child, and a right child's sibling is the parent's sibling's left child.

## 4. Approach (0:34) — `slides/04.png`

Step by step. First, recurse with parent and side. Second, save the old right child. Third, set right to the sibling. Fourth, recurse on children.

## 5. Java solution (0:47) — `slides/05.png`

Here's the Java solution, starting with right sibling tree. It follows the steps we just described.

## 6. Complexity (0:55) — `slides/06.png`

Time is O of n. Space is constant (iterative, besides an original-children snapshot per level).

## 7. Recap (1:01) — `slides/07.png`

To recap Right Sibling Tree: Process top-down: a left child's sibling is the right child, and a right child's sibling is the parent's sibling's left child. Try re-implementing it from scratch without looking.
