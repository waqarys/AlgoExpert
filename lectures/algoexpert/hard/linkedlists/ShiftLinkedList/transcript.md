# AlgoExpert · Shift Linked List

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Shift Linked List (0:00) — `slides/01.png`

Let's solve Shift Linked List, a hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Rotate the list k positions forward (k over 0) or backward (k under 0); return the new head.

## 3. Intuition (0:20) — `slides/03.png`

Rotation is just choosing a new tail: connect the old tail to the head and cut at length minus k.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Rotating one step at a time is n times k. Computing the length and cutting once is linear.

## 5. Approach (0:32) — `slides/05.png`

Step by step. First, find length and tail. Second, normalise k modulo length. Third, walk to the new tail. Fourth, rewire and return the new head.

## 6. Worked example (0:46) — `slides/06.png`

Find the length, 6, and the tail. Shifting by 2 is the same as 2 modulo the length.

## 7. Worked example (0:53) — `slides/07.png`

The new tail is 3 steps from the start: node 3. Its next, 4, becomes the new head.

## 8. Worked example (1:00) — `slides/08.png`

Cut after the new tail and connect the old tail to the old head.

## 9. Java solution (1:05) — `slides/09.png`

We walk to the tail counting length, compute the effective shift, walk to the new tail, cut, link the old tail to the old head, and return the new head.

## 10. Complexity (1:14) — `slides/10.png`

Time is O of n. Space is constant.

## 11. Edge cases & pitfalls (1:18) — `slides/11.png`

Take k mod length, using floor mod so negative k works.

## 12. Interview tips & follow-ups (1:22) — `slides/12.png`

This is rotate list.

## 13. Recap (1:25) — `slides/13.png`

To recap Shift Linked List: Rotation is just choosing a new tail: connect the old tail to the head and cut at length minus k. Try re-implementing it from scratch without looking.
