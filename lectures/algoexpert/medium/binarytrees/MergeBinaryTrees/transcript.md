# AlgoExpert · Merge Binary Trees

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merge Binary Trees (0:00) — `slides/01.png`

Let's solve Merge Binary Trees, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Overlay two trees; overlapping nodes sum their values. Mutates and returns tree1.

## 3. Intuition (0:20) — `slides/03.png`

Overlay the trees node by node: add values where both exist, otherwise keep whichever exists.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, if one tree is null, return the other. Second, add the values. Third, merge left children and right children.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with merge binary trees. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n of the smaller overlap. Space is O of h.

## 7. Recap (0:52) — `slides/07.png`

To recap Merge Binary Trees: Overlay the trees node by node: add values where both exist, otherwise keep whichever exists. Try re-implementing it from scratch without looking.
