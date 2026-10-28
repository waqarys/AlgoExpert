# AlgoExpert · Sum Bsts

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sum Bsts (0:00) — `slides/01.png`

Let's solve Sum Bsts, a hard binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sum the values of every node that roots a valid BST subtree containing at least 3 nodes. Post-order collecting (isBst, size, min, max, sum).

## 3. Intuition (0:24) — `slides/03.png`

Post-order lets each node know whether both children are BSTs, their sizes, sums and value ranges.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, return validity, size, sum, min and max from each subtree. Second, combine at the parent. Third, add sums of valid BSTs with three or more nodes.

## 5. Java solution (0:45) — `slides/05.png`

Here's the Java solution, starting with sum bsts. It follows the steps we just described.

## 6. Complexity (0:52) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:56) — `slides/07.png`

To recap Sum Bsts: Post-order lets each node know whether both children are BSTs, their sizes, sums and value ranges. Try re-implementing it from scratch without looking.
