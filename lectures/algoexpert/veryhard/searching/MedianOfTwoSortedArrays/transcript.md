# AlgoExpert · Median Of Two Sorted Arrays

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Median Of Two Sorted Arrays (0:00) — `slides/01.png`

Let's solve Median Of Two Sorted Arrays, a very hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Median of the union of two sorted arrays via binary-searched partition.

## 3. Intuition (0:19) — `slides/03.png`

Binary search a cut in the smaller array so the left halves of both hold exactly half the elements.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Merging is linear. Binary-searching a partition in the shorter array finds the median in log of the smaller length.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, search the cut in the smaller array. Second, derive the cut in the other. Third, check that the edges are in order. Fourth, median from the edge values.

## 6. Worked example (0:48) — `slides/06.png`

We want to cut both arrays so the left parts together have half the elements, and everything left is at most everything right.

## 7. Worked example (0:55) — `slides/07.png`

Binary search the cut in the shorter array. If b's left max exceeds a's right min, move a's cut right.

## 8. Worked example (1:02) — `slides/08.png`

Now the cut is valid. With an even total, the median is the average of the max left and min right: four point two five.

## 9. Java solution (1:11) — `slides/09.png`

We swap so a is shorter, binary search i, set j to half minus i, read the four border values with sentinels, adjust, and return the median when both conditions hold.

## 10. Complexity (1:21) — `slides/10.png`

Time is O(log(min(n, m))). Space is constant.

## 11. Edge cases & pitfalls (1:27) — `slides/11.png`

Always search the shorter array and use sentinels at the ends.

## 12. Interview tips & follow-ups (1:32) — `slides/12.png`

Explain the two cross conditions clearly.

## 13. Recap (1:35) — `slides/13.png`

To recap Median Of Two Sorted Arrays: Binary search a cut in the smaller array so the left halves of both hold exactly half the elements. Try re-implementing it from scratch without looking.
