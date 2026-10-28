# AlgoExpert · Maximize Expression

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Maximize Expression (0:00) — `slides/01.png`

Let's solve Maximize Expression, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Max of a - b plus c - d over indices a under b under c under d (0 if fewer than 4 elements). Four rolling DP layers.

## 3. Intuition (0:23) — `slides/03.png`

Build the expression one term at a time: best a, then best a minus b, and so on, each over a prefix.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

Checking every quadruple is n to the fourth. Building the expression in stages, max a, then max a minus b, and so on, is linear, and four running values suffice.

## 5. Approach (0:41) — `slides/05.png`

Step by step. First, four arrays of running bests. Second, each layer uses the previous layer up to the index before. Third, return the last layer's max.

## 6. Worked example (0:54) — `slides/06.png`

At 3, update each stage from the previous one, right to left. The best full expression so far is –.

## 7. Worked example (1:02) — `slides/07.png`

At 6, update each stage from the previous one, right to left. The best full expression so far is –.

## 8. Worked example (1:10) — `slides/08.png`

At 1, update each stage from the previous one, right to left. The best full expression so far is –.

## 9. Worked example (1:18) — `slides/09.png`

At -3, update each stage from the previous one, right to left. The best full expression so far is 1.

## 10. Worked example (1:26) — `slides/10.png`

At 2, update each stage from the previous one, right to left. The best full expression so far is 1.

## 11. Worked example (1:34) — `slides/11.png`

At 7, update each stage from the previous one, right to left. The best full expression so far is 4.

## 12. Java solution (1:42) — `slides/12.png`

We keep four stage values. For each index, update stage four from three minus x, three from two plus x, two from one minus x, and one from x.

## 13. Complexity (1:53) — `slides/13.png`

Time is O of n. Space is constant.

## 14. Edge cases & pitfalls (1:56) — `slides/14.png`

With fewer than four elements, return zero. Update in reverse stage order so each uses the previous index's values.

## 15. Interview tips & follow-ups (2:05) — `slides/15.png`

Explain the staged DP; it generalises to any alternating expression.

## 16. Recap (2:11) — `slides/16.png`

To recap Maximize Expression: Build the expression one term at a time: best a, then best a minus b, and so on, each over a prefix. Try re-implementing it from scratch without looking.
