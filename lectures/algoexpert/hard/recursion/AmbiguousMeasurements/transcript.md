# AlgoExpert · Ambiguous Measurements

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Ambiguous Measurements (0:00) — `slides/01.png`

Let's solve Ambiguous Measurements, a hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Measuring cups each measure a low, high range. Can repeated pours produce a volume within low, high ? Memoised search over remaining (low, high) targets.

## 3. Intuition (0:25) — `slides/03.png`

Try every cup recursively, shrinking the target range, and memoise the ranges already tried.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Trying every sequence of cups is exponential. Memoising on the remaining low and high bounds collapses repeats.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, if a cup fits inside the range, success. Second, otherwise subtract the cup from both bounds and recurse. Third, memoise by range.

## 6. Worked example (0:52) — `slides/06.png`

Each cup measures somewhere between its min and max. Can we guarantee a total between twenty-one hundred and twenty-three hundred?

## 7. Worked example (1:00) — `slides/07.png`

Using a cup shrinks the remaining range by its min and max. Recurse on the remaining range.

## 8. Worked example (1:06) — `slides/08.png`

We succeed when one cup's range fits inside the remaining range. The same remaining range repeats, so memoise on low and high.

## 9. Java solution (1:15) — `slides/09.png`

Can memoises on low and high. A cup succeeds if its range fits; otherwise we recurse with the range reduced by the cup, clamped at zero.

## 10. Complexity (1:24) — `slides/10.png`

Time is O of low times high times n. Space is O of low times high.

## 11. Edge cases & pitfalls (1:29) — `slides/11.png`

Clamp at zero, and skip cups that never make progress, to avoid infinite recursion.

## 12. Interview tips & follow-ups (1:35) — `slides/12.png`

Explain why low and high fully describe the state.

## 13. Recap (1:39) — `slides/13.png`

To recap Ambiguous Measurements: Try every cup recursively, shrinking the target range, and memoise the ranges already tried. Try re-implementing it from scratch without looking.
