# AlgoExpert · Bubble Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Bubble Sort (0:00) — `slides/01.png`

Let's solve Bubble Sort, an easy sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Repeatedly swap adjacent out-of-order pairs; stop early when a pass makes no swaps.

## 3. Intuition (0:18) — `slides/03.png`

Repeatedly swap neighbours that are out of order; each pass bubbles the largest remaining item to the end.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Bubble sort is quadratic, so in practice you'd use an n log n sort. Its one strength is the early exit: if a pass makes no swaps, the array is sorted, so already-sorted input takes linear time.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, loop until a pass makes no swaps. Second, swap adjacent pairs that are out of order. Third, shrink the range each pass.

## 6. Worked example (0:50) — `slides/06.png`

After pass 1, the largest remaining value, 9, has bubbled to position 6. Green cells are final.

## 7. Worked example (0:58) — `slides/07.png`

After pass 2, the largest remaining value, 8, has bubbled to position 5. Green cells are final.

## 8. Worked example (1:06) — `slides/08.png`

After pass 3, the largest remaining value, 6, has bubbled to position 4. Green cells are final.

## 9. Worked example (1:14) — `slides/09.png`

After pass 5, the largest remaining value, 5, has bubbled to position 2. Green cells are final.

## 10. Worked example (1:22) — `slides/10.png`

After pass 6, the largest remaining value, 3, has bubbled to position 1. Green cells are final.

## 11. Java solution (1:30) — `slides/11.png`

The outer loop repeats until no swaps happen. The inner loop compares each adjacent pair and swaps if out of order, and the range shrinks by one each pass.

## 12. Complexity (1:40) — `slides/12.png`

Time is O of n squared worst, O of n best. Space is constant.

## 13. Edge cases & pitfalls (1:46) — `slides/13.png`

Shrink the range each pass and stop early when nothing swaps. Bubble sort is stable, so equal elements keep their order.

## 14. Interview tips & follow-ups (1:54) — `slides/14.png`

Be ready to compare it with insertion and selection sort. The number of swaps equals the number of inversions.

## 15. Recap (2:02) — `slides/15.png`

To recap Bubble Sort: Repeatedly swap neighbours that are out of order; each pass bubbles the largest remaining item to the end. Try re-implementing it from scratch without looking.
