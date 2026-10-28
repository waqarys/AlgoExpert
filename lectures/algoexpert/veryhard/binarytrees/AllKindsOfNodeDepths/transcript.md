# AlgoExpert · All Kinds Of Node Depths

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. All Kinds Of Node Depths (0:00) — `slides/01.png`

Let's solve All Kinds Of Node Depths, a very hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Sum, over every node, of the depths of all nodes in its subtree (relative to it). Per subtree: sumDepths equals sumDepths(l) plus size(l) plus sumDepths(r) plus size(r).

## 3. Intuition (0:26) — `slides/03.png`

Each subtree's depth sum follows from its children's: their sums plus their sizes.

## 4. Brute force vs optimal (0:32) — `slides/04.png`

Computing each subtree's depth sum separately is quadratic. One post-order pass returning size, depth sum and total is linear.

## 5. Approach (0:41) — `slides/05.png`

Step by step. First, post-order returns size, depth sum and total. Second, depth sum equals children's sums plus their sizes. Third, add everyone's depth sums.

## 6. Worked example (0:54) — `slides/06.png`

Each node returns its subtree size, the sum of depths below it, and the running total.

## 7. Worked example (1:00) — `slides/07.png`

Moving up one level adds one to every node's depth below, so depth sum is children's sums plus their sizes.

## 8. Worked example (1:07) — `slides/08.png`

Adding every subtree's depth sum gives 26.

## 9. Java solution (1:11) — `slides/09.png`

Info returns zeros for null. Otherwise it combines children: size is one plus both, depths is each child's depth sum plus its size, and total adds the children's totals.

## 10. Complexity (1:22) — `slides/10.png`

Time is O of n. Space is O of h.

## 11. Edge cases & pitfalls (1:26) — `slides/11.png`

Use longs on big trees.

## 12. Interview tips & follow-ups (1:29) — `slides/12.png`

Explain why adding the size shifts depths by one.

## 13. Recap (1:33) — `slides/13.png`

To recap All Kinds Of Node Depths: Each subtree's depth sum follows from its children's: their sums plus their sizes. Try re-implementing it from scratch without looking.
