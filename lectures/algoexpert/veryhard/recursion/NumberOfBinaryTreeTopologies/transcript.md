# AlgoExpert · Number Of Binary Tree Topologies

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Number Of Binary Tree Topologies (0:00) — `slides/01.png`

Let's solve Number Of Binary Tree Topologies, a very hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Number of structurally distinct binary trees with n nodes (Catalan).

## 3. Intuition (0:19) — `slides/03.png`

Pick how many nodes go left; the counts multiply, giving the Catalan numbers.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Plain recursion recomputes sizes. A DP over sizes is quadratic, and the answer is the Catalan number.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, ways of zero is one. Second, for each n, sum left times right counts. Third, return ways of n.

## 6. Worked example (0:45) — `slides/06.png`

With 1 nodes, choose how many go left; multiply the left and right counts and sum: 1.

## 7. Worked example (0:51) — `slides/07.png`

With 2 nodes, choose how many go left; multiply the left and right counts and sum: 2.

## 8. Worked example (0:57) — `slides/08.png`

With 3 nodes, choose how many go left; multiply the left and right counts and sum: 5.

## 9. Worked example (1:03) — `slides/09.png`

With 4 nodes, choose how many go left; multiply the left and right counts and sum: 14.

## 10. Java solution (1:09) — `slides/10.png`

C of zero is one. For each m, sum c of left times c of m minus one minus left over all left sizes.

## 11. Complexity (1:17) — `slides/11.png`

Time is O of n squared. Space is O of n.

## 12. Edge cases & pitfalls (1:22) — `slides/12.png`

The empty tree counts as one topology.

## 13. Interview tips & follow-ups (1:26) — `slides/13.png`

Mention the closed form, two n choose n over n plus one.

## 14. Recap (1:31) — `slides/14.png`

To recap Number Of Binary Tree Topologies: Pick how many nodes go left; the counts multiply, giving the Catalan numbers. Try re-implementing it from scratch without looking.
