# AlgoExpert · Remove Duplicates From Linked List

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Remove Duplicates From Linked List (0:00) — `slides/01.png`

Let's solve Remove Duplicates From Linked List, an easy linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. List is sorted; remove nodes with repeated values in place.

## 3. Intuition (0:18) — `slides/03.png`

The list is sorted, so duplicates are adjacent; we can skip them in place.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, walk the list. Second, while the next node has the same value, bypass it. Third, move to the next distinct node. Fourth, return the head.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with remove duplicates from linked list. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:50) — `slides/07.png`

To recap Remove Duplicates From Linked List: The list is sorted, so duplicates are adjacent; we can skip them in place. Try re-implementing it from scratch without looking.
