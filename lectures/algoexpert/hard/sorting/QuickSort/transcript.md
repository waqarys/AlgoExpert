# AlgoExpert · Quick Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Quick Sort (0:00) — `slides/01.png`

Let's solve Quick Sort, a hard sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. In-place quicksort, recursing into the smaller partition first to bound stack depth.

## 3. Intuition (0:18) — `slides/03.png`

Partition around a pivot so smaller values go left and larger right, then sort each side.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Quadratic sorts compare everything. Quick sort partitions around a pivot and recurses, n log n on average.

## 5. Approach (0:32) — `slides/05.png`

Step by step. First, pick a pivot. Second, partition with two pointers. Third, recurse into the smaller side first. Fourth, loop on the larger to bound the stack.

## 6. Worked example (0:46) — `slides/06.png`

Partition indices 0 to 6 around 8: smaller to the left, larger to the right. It's now in its final spot, index 5.

## 7. Worked example (0:55) — `slides/07.png`

Partition indices 0 to 4 around 6: smaller to the left, larger to the right. It's now in its final spot, index 4.

## 8. Worked example (1:05) — `slides/08.png`

Partition indices 0 to 3 around 5: smaller to the left, larger to the right. It's now in its final spot, index 3.

## 9. Worked example (1:14) — `slides/09.png`

Partition indices 0 to 2 around 3: smaller to the left, larger to the right. It's now in its final spot, index 1.

## 10. Java solution (1:23) — `slides/10.png`

Sort loops while lo is below hi: partition, place the pivot at r, recurse on the smaller side and loop on the larger.

## 11. Complexity (1:31) — `slides/11.png`

Time is O of n log n avg, O of n squared worst. Space is O of log n.

## 12. Edge cases & pitfalls (1:37) — `slides/12.png`

Sorted input with a first-element pivot is quadratic; randomise. Recurse into the smaller side first to keep the stack logarithmic.

## 13. Interview tips & follow-ups (1:47) — `slides/13.png`

Three-way partitioning handles many duplicates well.

## 14. Recap (1:51) — `slides/14.png`

To recap Quick Sort: Partition around a pivot so smaller values go left and larger right, then sort each side. Try re-implementing it from scratch without looking.
