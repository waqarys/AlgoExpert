# AlgoExpert · Search In Sorted Matrix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Search In Sorted Matrix (0:00) — `slides/01.png`

Let's solve Search In Sorted Matrix, a medium searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Rows and columns are sorted ascending; return row, col of target or -1, -1 . Start top-right and eliminate a row or column each step.

## 3. Intuition (0:23) — `slides/03.png`

Start at the top-right: moving left decreases, moving down increases, so each step eliminates a row or column.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, start top-right. Second, if too big, move left. Third, if too small, move down. Fourth, return the coordinates or minus ones.

## 5. Java solution (0:44) — `slides/05.png`

Here's the Java solution, starting with search in sorted matrix. It follows the steps we just described.

## 6. Complexity (0:52) — `slides/06.png`

Time is O of n plus m. Space is constant.

## 7. Recap (0:56) — `slides/07.png`

To recap Search In Sorted Matrix: Start at the top-right: moving left decreases, moving down increases, so each step eliminates a row or column. Try re-implementing it from scratch without looking.
