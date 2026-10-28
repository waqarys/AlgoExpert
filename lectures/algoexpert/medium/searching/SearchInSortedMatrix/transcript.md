# AlgoExpert · Search In Sorted Matrix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Search In Sorted Matrix (0:00) — `slides/01.png`

Let's solve Search In Sorted Matrix, a medium searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Rows and columns are sorted ascending; return row, col of target or -1, -1 . Start top-right and eliminate a row or column each step.

## 3. Intuition (0:23) — `slides/03.png`

Start at the top-right: moving left decreases, moving down increases, so each step eliminates a row or column.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

Scanning everything ignores the sorting. Binary-searching each row is better. Starting at the top-right corner, every comparison eliminates a whole row or column, so it's r plus c.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, start top-right. Second, if too big, move left. Third, if too small, move down. Fourth, return the coordinates or minus ones.

## 6. Worked example (0:57) — `slides/06.png`

At 1000: too big, so everything below is too, move left.

## 7. Worked example (1:02) — `slides/07.png`

At 15: too small, so everything left is too, move down.

## 8. Worked example (1:07) — `slides/08.png`

At 32: too small, so everything left is too, move down.

## 9. Worked example (1:12) — `slides/09.png`

At 35: too small, so everything left is too, move down.

## 10. Worked example (1:17) — `slides/10.png`

At 45: too big, so everything below is too, move left.

## 11. Worked example (1:22) — `slides/11.png`

At 44: found it.

## 12. Java solution (1:25) — `slides/12.png`

We start at row zero and the last column. While in bounds, return on a match, move left if the value is too big, otherwise move down.

## 13. Complexity (1:34) — `slides/13.png`

Time is O of n plus m. Space is constant.

## 14. Edge cases & pitfalls (1:38) — `slides/14.png`

Top-right or bottom-left both work, because one move increases and the other decreases. From top-left both increase, so you can't decide.

## 15. Interview tips & follow-ups (1:48) — `slides/15.png`

Explain why the corner matters; that's the insight.

## 16. Recap (1:52) — `slides/16.png`

To recap Search In Sorted Matrix: Start at the top-right: moving left decreases, moving down increases, so each step eliminates a row or column. Try re-implementing it from scratch without looking.
