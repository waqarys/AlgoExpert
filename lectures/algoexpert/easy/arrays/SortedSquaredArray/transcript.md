# AlgoExpert · Sorted Squared Array

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sorted Squared Array (0:00) — `slides/01.png`

Let's solve Sorted Squared Array, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Given a sorted array (may contain negatives) return the squares in sorted order. Two pointers from both ends fill the result from the back.

## 3. Intuition (0:22) — `slides/03.png`

The largest squares sit at the two ends of a sorted array, because big negatives square to big positives.

## 4. Brute force vs optimal (0:29) — `slides/04.png`

The brute-force approach squares every value and sorts the result, which is n log n. But since the input is sorted, the largest square must come from one of the two ends, so two pointers fill the output from the back in linear time.

## 5. Approach (0:42) — `slides/05.png`

Step by step. First, put pointers at both ends. Second, compare absolute values. Third, write the larger square into the result from the back. Fourth, move that pointer inward.

## 6. Worked example (0:57) — `slides/06.png`

Compare the absolute values at the two ends. The right one, 8, is larger, so its square, 64, goes into position 4, and we move that pointer inward.

## 7. Worked example (1:08) — `slides/07.png`

Compare the absolute values at the two ends. The left one, -7, is larger, so its square, 49, goes into position 3, and we move that pointer inward.

## 8. Worked example (1:19) — `slides/08.png`

Compare the absolute values at the two ends. The right one, 4, is larger, so its square, 16, goes into position 2, and we move that pointer inward.

## 9. Worked example (1:30) — `slides/09.png`

Compare the absolute values at the two ends. The left one, -3, is larger, so its square, 9, goes into position 1, and we move that pointer inward.

## 10. Worked example (1:41) — `slides/10.png`

Compare the absolute values at the two ends. The right one, 1, is larger, so its square, 1, goes into position 0, and we move that pointer inward.

## 11. Java solution (1:52) — `slides/11.png`

We keep left and right pointers and an output array. Walking k from the last index down, we compare absolute values at both ends, write the larger square at k, and move that pointer inward.

## 12. Complexity (2:04) — `slides/12.png`

Time is O of n. Space is O of n.

## 13. Edge cases & pitfalls (2:07) — `slides/13.png`

Watch out for an all-negative input, where the order fully reverses, and remember that the output must be filled from the back, because we always find the largest remaining square.

## 14. Interview tips & follow-ups (2:17) — `slides/14.png`

Mention the sort-based solution first, then improve it. This is really a merge of two sorted sequences, the negatives reversed and the non-negatives, which is a nice way to explain it.

## 15. Recap (2:28) — `slides/15.png`

To recap Sorted Squared Array: The largest squares sit at the two ends of a sorted array, because big negatives square to big positives. Try re-implementing it from scratch without looking.
