# AlgoExpert · Rearrange Linked List

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Rearrange Linked List (0:00) — `slides/01.png`

Let's solve Rearrange Linked List, a very hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Stable partition around k: nodes under k, then equals equals k, then over k. Returns new head.

## 3. Intuition (0:21) — `slides/03.png`

Build three separate lists for less, equal and greater, then join them.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Three dummy-headed lists collect nodes in order, then concatenate, linear time and constant space.

## 5. Approach (0:32) — `slides/05.png`

Step by step. First, walk the list appending to the right partition. Second, keep heads and tails. Third, connect the non-empty lists.

## 6. Worked example (0:44) — `slides/06.png`

Rearrange so values less than 3 come first, then equal, then greater, keeping relative order.

## 7. Worked example (0:51) — `slides/07.png`

Walk once, appending each node to one of three lists.

## 8. Worked example (0:55) — `slides/08.png`

Join the three lists, carefully handling empty ones.

## 9. Java solution (0:59) — `slides/09.png`

We append each node to low, equal or high, terminate high, link equal to high, and low to equal or high if equal is empty.

## 10. Complexity (1:07) — `slides/10.png`

Time is O of n. Space is constant.

## 11. Edge cases & pitfalls (1:10) — `slides/11.png`

Terminate the high list with null, and skip empty partitions when linking.

## 12. Interview tips & follow-ups (1:15) — `slides/12.png`

Mention that it's stable.

## 13. Recap (1:18) — `slides/13.png`

To recap Rearrange Linked List: Build three separate lists for less, equal and greater, then join them. Try re-implementing it from scratch without looking.
