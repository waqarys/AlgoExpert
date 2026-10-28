# AlgoExpert · Branch Sums

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Branch Sums (0:00) — `slides/01.png`

Let's solve Branch Sums, an easy binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. List the root-to-leaf path sums, ordered left to right.

## 3. Intuition (0:17) — `slides/03.png`

Carry the running sum down each path; at a leaf, that sum is one branch sum.

## 4. Approach (0:22) — `slides/04.png`

Step by step. First, depth-first from the root with sum zero. Second, add the node's value. Third, at a leaf, record the sum. Fourth, recurse left then right to keep left-to-right order.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with branch sums. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:48) — `slides/07.png`

To recap Branch Sums: Carry the running sum down each path; at a leaf, that sum is one branch sum. Try re-implementing it from scratch without looking.
