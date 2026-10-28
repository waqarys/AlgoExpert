# AlgoExpert · Zip Linked List

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Zip Linked List (0:00) — `slides/01.png`

Let's solve Zip Linked List, a very hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Reorder in place to first, last, second, second-to-last, Split at middle, reverse second half, interleave.

## 3. Intuition (0:21) — `slides/03.png`

Split at the middle, reverse the back half, and interleave.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Storing nodes in an array is simple but uses space. Find the middle, reverse the second half, and interleave in place.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, find the middle. Second, reverse the second half. Third, alternate nodes from both halves.

## 6. Worked example (0:45) — `slides/06.png`

Find the middle with slow and fast pointers.

## 7. Worked example (0:48) — `slides/07.png`

Split there and reverse the second half.

## 8. Worked example (0:52) — `slides/08.png`

Interleave the two halves: one, six, two, five, three, four.

## 9. Java solution (0:58) — `slides/09.png`

We find the middle, cut, reverse the second half, then alternate links from each half.

## 10. Complexity (1:04) — `slides/10.png`

Time is O of n. Space is constant.

## 11. Edge cases & pitfalls (1:07) — `slides/11.png`

Cut the first half's tail, or you'll create a cycle.

## 12. Interview tips & follow-ups (1:12) — `slides/12.png`

This is reorder list.

## 13. Recap (1:15) — `slides/13.png`

To recap Zip Linked List: Split at the middle, reverse the back half, and interleave. Try re-implementing it from scratch without looking.
