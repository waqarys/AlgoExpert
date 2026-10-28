# AlgoExpert · Solve Sudoku

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Solve Sudoku (0:00) — `slides/01.png`

Let's solve Solve Sudoku, a hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Fill a 9 times 9 board (0 equals empty) in place via backtracking with row or col or box bitmasks.

## 3. Intuition (0:20) — `slides/03.png`

Backtracking with bitmasks of used digits per row, column and box makes each check constant time.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Trying every filling is astronomically large. Backtracking with row, column and box checks prunes almost everything. Bitmasks make each check constant time.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, record used digits. Second, find the next empty cell. Third, try each allowed digit and recurse. Fourth, undo on failure.

## 6. Worked example (0:51) — `slides/06.png`

Keep a bitmask of used digits for every row, column and three-by-three box, so checking a digit is constant time.

## 7. Worked example (0:59) — `slides/07.png`

At the first empty cell, the digits not used in its row, column or box are one, two and four. Try them in order.

## 8. Worked example (1:07) — `slides/08.png`

Place a digit and recurse to the next cell. If we hit a cell with no candidates, undo and try the next digit.

## 9. Java solution (1/2) (1:15) — `slides/09.png`

We initialise the masks from the given digits, then solve recursively over positions zero to eighty: skip filled cells, try each digit whose bit is free in row, column and box, set the bits, recurse, and clear on failure.

## 10. Java solution (2/2) (1:28) — `slides/10.png`

We initialise the masks from the given digits, then solve recursively over positions zero to eighty: skip filled cells, try each digit whose bit is free in row, column and box, set the bits, recurse, and clear on failure.

## 11. Complexity (1:40) — `slides/11.png`

Time is O of 9 to the empty worst. Space is constant besides recursion.

## 12. Edge cases & pitfalls (1:47) — `slides/12.png`

Always clear the bits when you backtrack.

## 13. Interview tips & follow-ups (1:51) — `slides/13.png`

Choosing the cell with the fewest candidates first speeds it up a lot.

## 14. Recap (1:55) — `slides/14.png`

To recap Solve Sudoku: Backtracking with bitmasks of used digits per row, column and box makes each check constant time. Try re-implementing it from scratch without looking.
