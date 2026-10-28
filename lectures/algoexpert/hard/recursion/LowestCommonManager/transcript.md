# AlgoExpert · Lowest Common Manager

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Lowest Common Manager (0:00) — `slides/01.png`

Let's solve Lowest Common Manager, a hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. In an org chart tree, the lowest manager having both reports somewhere beneath (or being one of them). Post-order counting of found reports.

## 3. Intuition (0:22) — `slides/03.png`

Post-order counts how many of the two reports each subtree contains; the first manager with both is the answer.

## 4. Brute force vs optimal (0:29) — `slides/04.png`

Building both paths from the top and comparing works. A single post-order pass that counts how many target reports each subtree contains finds the lowest common manager directly.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, recurse into reports. Second, count matches in each subtree. Third, the first node reaching two is the answer. Fourth, return it upward.

## 6. Worked example (0:54) — `slides/06.png`

Find the lowest manager above both E and I.

## 7. Worked example (0:58) — `slides/07.png`

Recursively, each manager returns how many of the two reports are in its subtree. D covers I, so one; E is itself one.

## 8. Worked example (1:07) — `slides/08.png`

B's subtree covers both, so B is the first manager to reach two. It's the answer, and we pass it upward unchanged.

## 9. Java solution (1:16) — `slides/09.png`

The helper visits each direct report, summing counts and returning early if a child already found the answer. It adds one if the current node is a target, and if the count hits two, records itself.

## 10. Complexity (1:28) — `slides/10.png`

Time is O of n. Space is O of d.

## 11. Edge cases & pitfalls (1:31) — `slides/11.png`

A report can itself be the manager of the other; the count still works.

## 12. Interview tips & follow-ups (1:36) — `slides/12.png`

This is lowest common ancestor generalised to n-ary trees.

## 13. Recap (1:41) — `slides/13.png`

To recap Lowest Common Manager: Post-order counts how many of the two reports each subtree contains; the first manager with both is the answer. Try re-implementing it from scratch without looking.
