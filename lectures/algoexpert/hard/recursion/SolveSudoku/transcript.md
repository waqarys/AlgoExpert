# AlgoExpert · Solve Sudoku

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Solve Sudoku (0:00) — `slides/01.png`

Let's solve Solve Sudoku, a hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Fill a 9 times 9 board (0 equals empty) in place via backtracking with row or col or box bitmasks.

## 3. Intuition (0:20) — `slides/03.png`

Backtracking with bitmasks of used digits per row, column and box makes each check constant time.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, record used digits. Second, find the next empty cell. Third, try each allowed digit and recurse. Fourth, undo on failure.

## 5. Java solution (1/2) (0:40) — `slides/05.png`

Here's the Java solution, starting with solve sudoku. It follows the steps we just described.

## 6. Java solution (2/2) (0:47) — `slides/06.png`

Continuing with solve.

## 7. Complexity (0:50) — `slides/07.png`

Time is O of 9 to the empty worst. Space is constant besides recursion.

## 8. Recap (0:57) — `slides/08.png`

To recap Solve Sudoku: Backtracking with bitmasks of used digits per row, column and box makes each check constant time. Try re-implementing it from scratch without looking.
