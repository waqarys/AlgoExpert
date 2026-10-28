# AlgoExpert · Largest Rectangle Under Skyline

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Largest Rectangle Under Skyline (0:00) — `slides/01.png`

Let's solve Largest Rectangle Under Skyline, a hard stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Largest rectangle area within adjacent buildings of width 1. Monotonic increasing stack of indices.

## 3. Intuition (0:21) — `slides/03.png`

A monotonic stack finds, for each building, how far it extends left and right before a shorter one.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Checking every range is quadratic. A monotonic increasing stack finds, for each bar, how far it can extend in both directions, and each bar is pushed and popped once.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, push indices with increasing heights. Second, when a shorter building arrives, pop and compute area. Third, width spans to the new top. Fourth, flush at the end.

## 6. Worked example (0:54) — `slides/06.png`

A lower bar arrives, so pop height 3. It extends from index 1 to 1, width 1, area 3, the best so far.

## 7. Worked example (1:03) — `slides/07.png`

A lower bar arrives, so pop height 3. It extends from index 1 to 2, width 2, area 6, the best so far.

## 8. Worked example (1:12) — `slides/08.png`

A lower bar arrives, so pop height 2. It extends from index 1 to 4, width 4, area 8, the best so far.

## 9. Worked example (1:21) — `slides/09.png`

A lower bar arrives, so pop height 1. It extends from index 0 to 8, width 9, area 9, the best so far.

## 10. Java solution (1:29) — `slides/10.png`

For i up to n, with height zero at the end, pop while the top is at least the current height, computing height times i minus new top minus one. Push i.

## 11. Complexity (1:39) — `slides/11.png`

Time is O of n. Space is O of n.

## 12. Edge cases & pitfalls (1:43) — `slides/12.png`

A zero sentinel at the end flushes remaining bars.

## 13. Interview tips & follow-ups (1:47) — `slides/13.png`

Apply it row by row for the maximal rectangle in a binary matrix.

## 14. Recap (1:52) — `slides/14.png`

To recap Largest Rectangle Under Skyline: A monotonic stack finds, for each building, how far it extends left and right before a shorter one. Try re-implementing it from scratch without looking.
