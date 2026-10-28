# AlgoExpert · Largest Range

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Largest Range (0:00) — `slides/01.png`

Let's solve Largest Range, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. lo, hi of the longest run of consecutive integers present in the array.

## 3. Intuition (0:18) — `slides/03.png`

Only start counting at a number that has no predecessor, so each run is scanned exactly once.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, put all numbers in a set. Second, for each number without number minus one, extend upward. Third, track the longest run's bounds.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with largest range. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:48) — `slides/07.png`

To recap Largest Range: Only start counting at a number that has no predecessor, so each run is scanned exactly once. Try re-implementing it from scratch without looking.
