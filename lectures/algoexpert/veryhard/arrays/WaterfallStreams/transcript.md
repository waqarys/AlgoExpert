# AlgoExpert · Waterfall Streams

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Waterfall Streams (0:00) — `slides/01.png`

Let's solve Waterfall Streams, a very hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Water poured at the top of source column falls through a grid of 0 (air) and 1 (block). On hitting a block it splits half left, half right, flowing sideways until it can fall (or is lost at a wall). Return percentages reaching each bottom-row column. Row-by-row simulation.

## 3. Intuition (0:31) — `slides/03.png`

Simulate row by row: water above a block splits left and right until it finds a gap to fall through.

## 4. Brute force vs optimal (0:38) — `slides/04.png`

Simulating individual droplets is slow. Carrying amounts row by row, splitting on blocks, is simple and fast enough.

## 5. Approach (0:46) — `slides/05.png`

Step by step. First, carry percentages per column. Second, on a block, split half left and half right. Third, each half moves until a gap or a wall. Fourth, return the bottom row.

## 6. Worked example (1:02) — `slides/06.png`

Water falls straight down from the source until it hits a block.

## 7. Worked example (1:06) — `slides/07.png`

On a block, it splits in half, and each half flows sideways until it can fall again, or is trapped by a wall.

## 8. Worked example (1:13) — `slides/08.png`

Row by row, we carry water amounts down. The bottom row's amounts, as percentages, are the answer.

## 9. Java solution (1:21) — `slides/09.png`

For each row, water above an open cell falls in; above a block, it splits and each half moves sideways until there's an opening above the next row or a block stops it. Finally we scale the last row to percentages.

## 10. Complexity (1:34) — `slides/10.png`

Time is O of w squared times h. Space is O of w.

## 11. Edge cases & pitfalls (1:38) — `slides/11.png`

Water that hits a side wall is lost.

## 12. Interview tips & follow-ups (1:42) — `slides/12.png`

Draw a small grid first.

## 13. Recap (1:45) — `slides/13.png`

To recap Waterfall Streams: Simulate row by row: water above a block splits left and right until it finds a gap to fall through. Try re-implementing it from scratch without looking.
