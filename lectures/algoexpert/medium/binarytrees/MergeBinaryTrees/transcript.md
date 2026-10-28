# AlgoExpert · Merge Binary Trees

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merge Binary Trees (0:00) — `slides/01.png`

Let's solve Merge Binary Trees, a medium binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Overlay two trees; overlapping nodes sum their values. Mutates and returns tree1.

## 3. Intuition (0:20) — `slides/03.png`

Overlay the trees node by node: add values where both exist, otherwise keep whichever exists.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Building a new tree copies everything. Merging into the first tree in place is cheaper: we only recurse where both trees have nodes, and reuse a subtree whenever one side is missing.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, if one tree is null, return the other. Second, add the values. Third, merge left children and right children.

## 6. Worked example (0:49) — `slides/06.png`

We overlay two trees: where both have a node, add the values; otherwise keep whichever exists.

## 7. Worked example (0:56) — `slides/07.png`

Root one plus one gives two; three plus five gives eight; two plus nine gives eleven; seven plus two gives nine.

## 8. Worked example (1:03) — `slides/08.png`

Where only one tree has a node, like four from tree one, or seven and six from tree two, we simply reuse that subtree.

## 9. Java solution (1:11) — `slides/09.png`

If either tree is null, return the other. Otherwise add the second value into the first, merge the left children, merge the right children, and return the first tree.

## 10. Complexity (1:22) — `slides/10.png`

Time is O of n of the smaller overlap. Space is O of h.

## 11. Edge cases & pitfalls (1:28) — `slides/11.png`

Handle either tree being null, and mention that the result mutates and shares structure with the inputs.

## 12. Interview tips & follow-ups (1:34) — `slides/12.png`

Ask whether modifying the inputs is acceptable; otherwise build new nodes.

## 13. Recap (1:39) — `slides/13.png`

To recap Merge Binary Trees: Overlay the trees node by node: add values where both exist, otherwise keep whichever exists. Try re-implementing it from scratch without looking.
