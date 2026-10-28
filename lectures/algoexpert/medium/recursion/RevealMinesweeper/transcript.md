# AlgoExpert · Reveal Minesweeper

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Reveal Minesweeper (0:00) — `slides/01.png`

Let's solve Reveal Minesweeper, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Board of "M" (mine), "H" (hidden), "0"-"8" (revealed). Clicking a mine sets it to "X"; clicking a hidden cell reveals its adjacent-mine count and, if zero, recursively reveals neighbours.

## 3. Intuition (0:26) — `slides/03.png`

Clicking a mine ends the game; clicking an empty square reveals neighbours recursively.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

If the click is a mine, mark it and stop. Otherwise count adjacent mines; if there are none, recursively reveal every neighbour. Each cell is revealed at most once.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, if a mine, mark X. Second, count adjacent mines. Third, if zero, reveal neighbours recursively. Fourth, otherwise show the count.

## 6. Worked example (0:57) — `slides/06.png`

Cell row 0, column 3 has 0 adjacent mines. Zero, so we reveal all its neighbours.

## 7. Worked example (1:05) — `slides/07.png`

Cell row 0, column 2 has 1 adjacent mines. Non-zero, so we stop here.

## 8. Worked example (1:12) — `slides/08.png`

Cell row 1, column 2 has 1 adjacent mines. Non-zero, so we stop here.

## 9. Worked example (1:19) — `slides/09.png`

Cell row 1, column 3 has 0 adjacent mines. Zero, so we reveal all its neighbours.

## 10. Worked example (1:26) — `slides/10.png`

Cell row 2, column 2 has 2 adjacent mines. Non-zero, so we stop here.

## 11. Worked example (1:33) — `slides/11.png`

Cell row 2, column 3 has 1 adjacent mines. Non-zero, so we stop here.

## 12. Java solution (1:40) — `slides/12.png`

If the clicked cell is a mine we mark it X. Reveal returns for non-hidden cells, counts mines in the eight neighbours, writes the count, and recurses on neighbours only when the count is zero.

## 13. Complexity (1:51) — `slides/13.png`

Time is O of w times h. Space is O of w times h.

## 14. Edge cases & pitfalls (1:56) — `slides/14.png`

Neighbours include diagonals. Only hidden cells recurse, which prevents infinite loops, and only zero cells spread.

## 15. Interview tips & follow-ups (2:04) — `slides/15.png`

On huge boards, a queue avoids deep recursion.

## 16. Recap (2:08) — `slides/16.png`

To recap Reveal Minesweeper: Clicking a mine ends the game; clicking an empty square reveals neighbours recursively. Try re-implementing it from scratch without looking.
