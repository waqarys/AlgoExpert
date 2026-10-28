# AlgoExpert · Repair Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Repair Bst (0:00) — `slides/01.png`

Let's solve Repair Bst, a hard binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Exactly two nodes' values were swapped; swap them back in place. Iterative in-order finds the two out-of-order nodes.

## 3. Intuition (0:22) — `slides/03.png`

An in-order traversal of a BST is sorted; the two swapped nodes show up as order violations.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Dumping the in-order traversal into an array, sorting it and writing it back uses linear space. Tracking the previous node during an in-order walk spots the violations with only the stack.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, in-order traverse tracking the previous node. Second, the first violation gives the first node. Third, the last violation gives the second. Fourth, swap their values.

## 6. Worked example (0:55) — `slides/06.png`

Two values in this BST were swapped. We need to find and fix them.

## 7. Worked example (1:01) — `slides/07.png`

An in-order traversal of a BST is sorted. Here it drops: the first is the larger value before the first drop, 12, and the second is the smaller value after the last drop, 7.

## 8. Worked example (1:13) — `slides/08.png`

Swap those two values back and the in-order traversal is sorted again.

## 9. Java solution (1:18) — `slides/09.png`

We do an iterative in-order traversal. When prev is greater than cur, the first time we record prev as first, and every time we record cur as second. Finally we swap their values.

## 10. Complexity (1:31) — `slides/10.png`

Time is O of n. Space is O of h.

## 11. Edge cases & pitfalls (1:35) — `slides/11.png`

If the swapped nodes are adjacent in order, there's only one drop; the rule still works.

## 12. Interview tips & follow-ups (1:41) — `slides/12.png`

Mention Morris traversal for constant space.

## 13. Recap (1:45) — `slides/13.png`

To recap Repair Bst: An in-order traversal of a BST is sorted; the two swapped nodes show up as order violations. Try re-implementing it from scratch without looking.
