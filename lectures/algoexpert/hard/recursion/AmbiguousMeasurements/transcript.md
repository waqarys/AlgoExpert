# AlgoExpert · Ambiguous Measurements

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Ambiguous Measurements (0:00) — `slides/01.png`

Let's solve Ambiguous Measurements, a hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Measuring cups each measure a low, high range. Can repeated pours produce a volume within low, high ? Memoised search over remaining (low, high) targets.

## 3. Intuition (0:25) — `slides/03.png`

Try every cup recursively, shrinking the target range, and memoise the ranges already tried.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, if a cup fits inside the range, success. Second, otherwise subtract the cup from both bounds and recurse. Third, memoise by range.

## 5. Java solution (0:44) — `slides/05.png`

Here's the Java solution, starting with ambiguous measurements. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of low times high times n. Space is O of low times high.

## 7. Recap (0:56) — `slides/07.png`

To recap Ambiguous Measurements: Try every cup recursively, shrinking the target range, and memoise the ranges already tried. Try re-implementing it from scratch without looking.
