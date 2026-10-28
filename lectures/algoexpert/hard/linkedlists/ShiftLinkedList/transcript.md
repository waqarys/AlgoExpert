# AlgoExpert · Shift Linked List

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Shift Linked List (0:00) — `slides/01.png`

Let's solve Shift Linked List, a hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Rotate the list k positions forward (k over 0) or backward (k under 0); return the new head.

## 3. Intuition (0:20) — `slides/03.png`

Rotation is just choosing a new tail: connect the old tail to the head and cut at length minus k.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, find length and tail. Second, normalise k modulo length. Third, walk to the new tail. Fourth, rewire and return the new head.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with shift linked list. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Shift Linked List: Rotation is just choosing a new tail: connect the old tail to the head and cut at length minus k. Try re-implementing it from scratch without looking.
