# AlgoExpert · All Kinds Of Node Depths

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. All Kinds Of Node Depths (0:00) — `slides/01.png`

Let's solve All Kinds Of Node Depths, a very hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Sum, over every node, of the depths of all nodes in its subtree (relative to it). Per subtree: sumDepths equals sumDepths(l) plus size(l) plus sumDepths(r) plus size(r).

## 3. Intuition (0:26) — `slides/03.png`

Each subtree's depth sum follows from its children's: their sums plus their sizes.

## 4. Approach (0:32) — `slides/04.png`

Step by step. First, post-order returns size, depth sum and total. Second, depth sum equals children's sums plus their sizes. Third, add everyone's depth sums.

## 5. Java solution (0:45) — `slides/05.png`

Here's the Java solution, starting with all kinds of node depths. It follows the steps we just described.

## 6. Complexity (0:53) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:56) — `slides/07.png`

To recap All Kinds Of Node Depths: Each subtree's depth sum follows from its children's: their sums plus their sizes. Try re-implementing it from scratch without looking.
