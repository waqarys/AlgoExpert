# AlgoExpert · Merge Linked Lists

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merge Linked Lists (0:00) — `slides/01.png`

Let's solve Merge Linked Lists, a hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Merge two sorted lists in place; return the head of the merged list.

## 3. Intuition (0:18) — `slides/03.png`

Walk both sorted lists, splicing the smaller node in front each time, without new nodes.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, keep pointers into both lists and a previous pointer. Second, splice the smaller node. Third, attach any leftover tail. Fourth, return the smaller head.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with merge linked lists. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n plus m. Space is constant.

## 7. Recap (0:50) — `slides/07.png`

To recap Merge Linked Lists: Walk both sorted lists, splicing the smaller node in front each time, without new nodes. Try re-implementing it from scratch without looking.
