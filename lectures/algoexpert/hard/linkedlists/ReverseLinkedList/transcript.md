# AlgoExpert · Reverse Linked List

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Reverse Linked List (0:00) — `slides/01.png`

Let's solve Reverse Linked List, a hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Reverse in place and return the new head.

## 3. Intuition (0:17) — `slides/03.png`

Flip each link to point backwards, keeping three pointers so nothing is lost.

## 4. Approach (0:22) — `slides/04.png`

Step by step. First, previous starts null. Second, save next, point current at previous. Third, advance both. Fourth, previous is the new head.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with reverse linked list. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:47) — `slides/07.png`

To recap Reverse Linked List: Flip each link to point backwards, keeping three pointers so nothing is lost. Try re-implementing it from scratch without looking.
