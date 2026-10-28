# AlgoExpert · Reveal Minesweeper

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Reveal Minesweeper (0:00) — `slides/01.png`

Let's solve Reveal Minesweeper, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Board of "M" (mine), "H" (hidden), "0"-"8" (revealed). Clicking a mine sets it to "X"; clicking a hidden cell reveals its adjacent-mine count and, if zero, recursively reveals neighbours.

## 3. Intuition (0:26) — `slides/03.png`

Clicking a mine ends the game; clicking an empty square reveals neighbours recursively.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, if a mine, mark X. Second, count adjacent mines. Third, if zero, reveal neighbours recursively. Fourth, otherwise show the count.

## 5. Java solution (0:45) — `slides/05.png`

Here's the Java solution, starting with reveal minesweeper. It follows the steps we just described.

## 6. Complexity (0:53) — `slides/06.png`

Time is O of w times h. Space is O of w times h.

## 7. Recap (0:58) — `slides/07.png`

To recap Reveal Minesweeper: Clicking a mine ends the game; clicking an empty square reveals neighbours recursively. Try re-implementing it from scratch without looking.
