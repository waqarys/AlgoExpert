# AlgoExpert · Remove Duplicates From Linked List

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Remove Duplicates From Linked List (0:00) — `slides/01.png`

Let's solve Remove Duplicates From Linked List, an easy linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. List is sorted; remove nodes with repeated values in place.

## 3. Intuition (0:18) — `slides/03.png`

The list is sorted, so duplicates are adjacent; we can skip them in place.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

A hash set would work even for unsorted lists, but costs extra space. Because this list is sorted, duplicates are always adjacent, so we can just skip over them in place.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, walk the list. Second, while the next node has the same value, bypass it. Third, move to the next distinct node. Fourth, return the head.

## 6. Worked example (0:49) — `slides/06.png`

At value 1, the next 1 node is the same, so we bypass it.

## 7. Worked example (0:54) — `slides/07.png`

At value 3, the next node is different, so we just move on.

## 8. Worked example (0:59) — `slides/08.png`

At value 4, the next 2 nodes are the same, so we bypass them.

## 9. Worked example (1:03) — `slides/09.png`

At value 5, the next node is different, so we just move on.

## 10. Worked example (1:08) — `slides/10.png`

At value 6, the next 1 node is the same, so we bypass it.

## 11. Java solution (1:13) — `slides/11.png`

For each node, we find the next node with a different value, point current dot next at it, and move current forward.

## 12. Complexity (1:20) — `slides/12.png`

Time is O of n. Space is constant.

## 13. Edge cases & pitfalls (1:24) — `slides/13.png`

Handle long runs of duplicates with an inner loop, not a single skip, and make sure the end of the list works.

## 14. Interview tips & follow-ups (1:31) — `slides/14.png`

A tricky follow-up removes every value that had duplicates entirely. For unsorted lists, use a hash set.

## 15. Recap (1:39) — `slides/15.png`

To recap Remove Duplicates From Linked List: The list is sorted, so duplicates are adjacent; we can skip them in place. Try re-implementing it from scratch without looking.
