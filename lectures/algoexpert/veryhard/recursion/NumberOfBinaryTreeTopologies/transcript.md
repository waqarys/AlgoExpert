# AlgoExpert · Number Of Binary Tree Topologies

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Number Of Binary Tree Topologies (0:00) — `slides/01.png`

Let's solve Number Of Binary Tree Topologies, a very hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Number of structurally distinct binary trees with n nodes (Catalan).

## 3. Intuition (0:19) — `slides/03.png`

Pick how many nodes go left; the counts multiply, giving the Catalan numbers.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, ways of zero is one. Second, for each n, sum left times right counts. Third, return ways of n.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with number of binary tree topologies. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n squared. Space is O of n.

## 7. Recap (0:50) — `slides/07.png`

To recap Number Of Binary Tree Topologies: Pick how many nodes go left; the counts multiply, giving the Catalan numbers. Try re-implementing it from scratch without looking.
