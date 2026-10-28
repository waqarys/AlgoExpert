# AlgoExpert · Merge Linked Lists

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merge Linked Lists (0:00) — `slides/01.png`

Let's solve Merge Linked Lists, a hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Merge two sorted lists in place; return the head of the merged list.

## 3. Intuition (0:18) — `slides/03.png`

Walk both sorted lists, splicing the smaller node in front each time, without new nodes.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Copying everything and sorting ignores that both lists are sorted. A merge with a dummy head relinks nodes in linear time and constant space.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, keep pointers into both lists and a previous pointer. Second, splice the smaller node. Third, attach any leftover tail. Fourth, return the smaller head.

## 6. Worked example (0:48) — `slides/06.png`

Compare the heads; the smaller, 1, comes from the second list.

## 7. Worked example (0:53) — `slides/07.png`

Compare the heads; the smaller, 2, comes from the first list.

## 8. Worked example (0:58) — `slides/08.png`

Compare the heads; the smaller, 4, comes from the second list.

## 9. Worked example (1:03) — `slides/09.png`

Compare the heads; the smaller, 6, comes from the first list.

## 10. Worked example (1:08) — `slides/10.png`

Compare the heads; the smaller, 8, comes from the first list.

## 11. Worked example (1:12) — `slides/11.png`

When one list runs out, attach the rest of the other in one step.

## 12. Java solution (1:17) — `slides/12.png`

With a dummy tail we repeatedly link the smaller head and advance. Then we attach whichever list remains and return dummy's next.

## 13. Complexity (1:26) — `slides/13.png`

Time is O of n plus m. Space is constant.

## 14. Edge cases & pitfalls (1:30) — `slides/14.png`

Handle empty inputs, and attach the leftover in one assignment.

## 15. Interview tips & follow-ups (1:35) — `slides/15.png`

Merging k lists uses a heap.

## 16. Recap (1:38) — `slides/16.png`

To recap Merge Linked Lists: Walk both sorted lists, splicing the smaller node in front each time, without new nodes. Try re-implementing it from scratch without looking.
