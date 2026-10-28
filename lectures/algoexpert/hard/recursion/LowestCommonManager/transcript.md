# AlgoExpert · Lowest Common Manager

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Lowest Common Manager (0:00) — `slides/01.png`

Let's solve Lowest Common Manager, a hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. In an org chart tree, the lowest manager having both reports somewhere beneath (or being one of them). Post-order counting of found reports.

## 3. Intuition (0:22) — `slides/03.png`

Post-order counts how many of the two reports each subtree contains; the first manager with both is the answer.

## 4. Approach (0:29) — `slides/04.png`

Step by step. First, recurse into reports. Second, count matches in each subtree. Third, the first node reaching two is the answer. Fourth, return it upward.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with org chart. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n. Space is O of d.

## 7. Recap (0:54) — `slides/07.png`

To recap Lowest Common Manager: Post-order counts how many of the two reports each subtree contains; the first manager with both is the answer. Try re-implementing it from scratch without looking.
