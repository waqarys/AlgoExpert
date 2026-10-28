# AlgoExpert · Merge Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merge Sort (0:00) — `slides/01.png`

Let's solve Merge Sort, a very hard sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Stable divide-and-conquer sort using one auxiliary buffer.

## 3. Intuition (0:17) — `slides/03.png`

Split in half, sort each half, then merge the sorted halves.

## 4. Brute force vs optimal (0:22) — `slides/04.png`

Merge sort guarantees n log n and is stable, at the cost of an auxiliary array.

## 5. Approach (0:28) — `slides/05.png`

Step by step. First, recurse on halves. Second, merge using a buffer. Third, copy back.

## 6. Worked example (0:38) — `slides/06.png`

Split the array in half repeatedly until pieces have one element.

## 7. Worked example (0:43) — `slides/07.png`

After recursion, both halves are sorted.

## 8. Worked example (0:46) — `slides/08.png`

Merge by repeatedly taking the smaller front element.

## 9. Java solution (0:51) — `slides/09.png`

Sort recurses on both halves, copies the range to aux, and merges back taking the smaller of the two fronts.

## 10. Complexity (0:58) — `slides/10.png`

Time is O of n log n. Space is O of n.

## 11. Edge cases & pitfalls (1:02) — `slides/11.png`

Allocate the auxiliary array once, not per call.

## 12. Interview tips & follow-ups (1:06) — `slides/12.png`

Contrast with quick sort's average speed and in-place nature.

## 13. Recap (1:10) — `slides/13.png`

To recap Merge Sort: Split in half, sort each half, then merge the sorted halves. Try re-implementing it from scratch without looking.
