# AlgoExpert · Maximize Expression

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Maximize Expression (0:00) — `slides/01.png`

Let's solve Maximize Expression, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Max of a - b plus c - d over indices a under b under c under d (0 if fewer than 4 elements). Four rolling DP layers.

## 3. Intuition (0:23) — `slides/03.png`

Build the expression one term at a time: best a, then best a minus b, and so on, each over a prefix.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, four arrays of running bests. Second, each layer uses the previous layer up to the index before. Third, return the last layer's max.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with maximize expression. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:54) — `slides/07.png`

To recap Maximize Expression: Build the expression one term at a time: best a, then best a minus b, and so on, each over a prefix. Try re-implementing it from scratch without looking.
