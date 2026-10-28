# AlgoExpert · Line Through Points

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Line Through Points (0:00) — `slides/01.png`

Let's solve Line Through Points, a very hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Maximum number of the given (unique, integer) points lying on one straight line. For each anchor, count normalised slopes (reduced by gcd, sign-canonicalised).

## 3. Intuition (0:24) — `slides/03.png`

Fix an anchor point; points on the same line through it share a normalised slope.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, for each anchor, map slopes to counts. Second, normalise slopes with gcd and sign. Third, track the largest count plus one.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with line through points. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n squared. Space is O of n.

## 7. Recap (0:55) — `slides/07.png`

To recap Line Through Points: Fix an anchor point; points on the same line through it share a normalised slope. Try re-implementing it from scratch without looking.
