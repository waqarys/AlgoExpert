# AlgoExpert · Waterfall Streams

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Waterfall Streams (0:00) — `slides/01.png`

Let's solve Waterfall Streams, a very hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Water poured at the top of source column falls through a grid of 0 (air) and 1 (block). On hitting a block it splits half left, half right, flowing sideways until it can fall (or is lost at a wall). Return percentages reaching each bottom-row column. Row-by-row simulation.

## 3. Intuition (0:31) — `slides/03.png`

Simulate row by row: water above a block splits left and right until it finds a gap to fall through.

## 4. Approach (0:38) — `slides/04.png`

Step by step. First, carry percentages per column. Second, on a block, split half left and half right. Third, each half moves until a gap or a wall. Fourth, return the bottom row.

## 5. Java solution (0:53) — `slides/05.png`

Here's the Java solution, starting with waterfall streams. It follows the steps we just described.

## 6. Complexity (1:00) — `slides/06.png`

Time is O of w squared times h. Space is O of w.

## 7. Recap (1:05) — `slides/07.png`

To recap Waterfall Streams: Simulate row by row: water above a block splits left and right until it finds a gap to fall through. Try re-implementing it from scratch without looking.
