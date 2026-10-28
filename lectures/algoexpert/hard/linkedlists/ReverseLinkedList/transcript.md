# AlgoExpert · Reverse Linked List

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Reverse Linked List (0:00) — `slides/01.png`

Let's solve Reverse Linked List, a hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Reverse in place and return the new head.

## 3. Intuition (0:17) — `slides/03.png`

Flip each link to point backwards, keeping three pointers so nothing is lost.

## 4. Brute force vs optimal (0:22) — `slides/04.png`

Rebuilding from an array uses extra memory. The iterative version flips one pointer at a time with prev, current and next.

## 5. Approach (0:31) — `slides/05.png`

Step by step. First, previous starts null. Second, save next, point current at previous. Third, advance both. Fourth, previous is the new head.

## 6. Worked example (0:45) — `slides/06.png`

After reversing 0 nodes, prev heads nothing and the remaining list starts at 0.

## 7. Worked example (0:51) — `slides/07.png`

After reversing 2 nodes, prev heads 1 and the remaining list starts at 2.

## 8. Worked example (0:56) — `slides/08.png`

After reversing 4 nodes, prev heads 3 and the remaining list starts at 4.

## 9. Worked example (1:02) — `slides/09.png`

After reversing 6 nodes, prev heads 5 and the remaining list starts at null.

## 10. Java solution (1:08) — `slides/10.png`

While head isn't null, save next, point head at prev, move prev to head and head to next. Return prev.

## 11. Complexity (1:16) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:20) — `slides/12.png`

Save next before you overwrite the pointer, and return prev at the end.

## 13. Interview tips & follow-ups (1:26) — `slides/13.png`

A follow-up reverses in groups of k.

## 14. Recap (1:29) — `slides/14.png`

To recap Reverse Linked List: Flip each link to point backwards, keeping three pointers so nothing is lost. Try re-implementing it from scratch without looking.
