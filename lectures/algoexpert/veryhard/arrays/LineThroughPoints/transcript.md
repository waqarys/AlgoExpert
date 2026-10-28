# AlgoExpert · Line Through Points

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Line Through Points (0:00) — `slides/01.png`

Let's solve Line Through Points, a very hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Maximum number of the given (unique, integer) points lying on one straight line. For each anchor, count normalised slopes (reduced by gcd, sign-canonicalised).

## 3. Intuition (0:24) — `slides/03.png`

Fix an anchor point; points on the same line through it share a normalised slope.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

Checking each pair's line against every point is cubic. Anchoring at each point and grouping the others by slope is quadratic.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, for each anchor, map slopes to counts. Second, normalise slopes with gcd and sign. Third, track the largest count plus one.

## 6. Worked example (0:51) — `slides/06.png`

Anchor at (1, 1): group the other points by reduced slope. The biggest group plus the anchor gives 3 points on one line. Best so far 3.

## 7. Worked example (1:01) — `slides/07.png`

Anchor at (2, 2): group the other points by reduced slope. The biggest group plus the anchor gives 4 points on one line. Best so far 4.

## 8. Worked example (1:12) — `slides/08.png`

Anchor at (3, 3): group the other points by reduced slope. The biggest group plus the anchor gives 2 points on one line. Best so far 4.

## 9. Java solution (1:23) — `slides/09.png`

For each anchor, we compute reduced dx and dy to every later point, normalise the sign, count in a map, and track the best count plus one.

## 10. Complexity (1:32) — `slides/10.png`

Time is O of n squared. Space is O of n.

## 11. Edge cases & pitfalls (1:37) — `slides/11.png`

Floating-point slopes are risky; use reduced integer pairs with normalised signs.

## 12. Interview tips & follow-ups (1:42) — `slides/12.png`

If duplicates are allowed, count them separately.

## 13. Recap (1:46) — `slides/13.png`

To recap Line Through Points: Fix an anchor point; points on the same line through it share a normalised slope. Try re-implementing it from scratch without looking.
