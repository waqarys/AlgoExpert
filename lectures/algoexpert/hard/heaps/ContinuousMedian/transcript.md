# AlgoExpert · Continuous Median

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Continuous Median (0:00) — `slides/01.png`

Let's solve Continuous Median, a hard heaps problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Insert numbers one at a time and query the running median, using a max-heap for the lower half and a min-heap for the upper half.

## 3. Intuition (0:20) — `slides/03.png`

Keep the smaller half in a max-heap and the larger half in a min-heap, balanced in size.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Inserting into a sorted list is linear each time. Two heaps, a max-heap for the lower half and a min-heap for the upper, give log n inserts and constant-time median.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, insert into the right heap. Second, rebalance so sizes differ by at most one. Third, median is the top of the bigger heap or the average of tops.

## 6. Worked example (0:50) — `slides/06.png`

Insert 5 into the lower half and rebalance so the sizes differ by at most one. The median is 5.

## 7. Worked example (0:58) — `slides/07.png`

Insert 10 into the upper half and rebalance so the sizes differ by at most one. The median is 7.5.

## 8. Worked example (1:06) — `slides/08.png`

Insert 100 into the upper half and rebalance so the sizes differ by at most one. The median is 10.

## 9. Worked example (1:14) — `slides/09.png`

Insert 6 into the lower half and rebalance so the sizes differ by at most one. The median is 10.

## 10. Worked example (1:22) — `slides/10.png`

Insert 13 into the upper half and rebalance so the sizes differ by at most one. The median is 11.5.

## 11. Worked example (1:30) — `slides/11.png`

Insert 14 into the upper half and rebalance so the sizes differ by at most one. The median is 13.

## 12. Java solution (1:38) — `slides/12.png`

Insert adds to the lower heap if empty or smaller than its top, otherwise upper. Then we move one element if sizes differ by two, and compute the median from the tops.

## 13. Complexity (1:49) — `slides/13.png`

Time is O of log n insert, constant median. Space is O of n.

## 14. Edge cases & pitfalls (1:55) — `slides/14.png`

Rebalance after every insert, and average the two tops when the sizes are equal.

## 15. Interview tips & follow-ups (2:01) — `slides/15.png`

A follow-up is the sliding-window median, which needs deletions.

## 16. Recap (2:06) — `slides/16.png`

To recap Continuous Median: Keep the smaller half in a max-heap and the larger half in a min-heap, balanced in size. Try re-implementing it from scratch without looking.
