# AlgoExpert · Rearrange Linked List

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Rearrange Linked List (0:00) — `slides/01.png`

Let's solve Rearrange Linked List, a very hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Stable partition around k: nodes under k, then equals equals k, then over k. Returns new head.

## 3. Intuition (0:21) — `slides/03.png`

Build three separate lists for less, equal and greater, then join them.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, walk the list appending to the right partition. Second, keep heads and tails. Third, connect the non-empty lists.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with rearrange linked list. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:49) — `slides/07.png`

To recap Rearrange Linked List: Build three separate lists for less, equal and greater, then join them. Try re-implementing it from scratch without looking.
