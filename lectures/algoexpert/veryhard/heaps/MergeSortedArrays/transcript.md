# AlgoExpert · Merge Sorted Arrays

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merge Sorted Arrays (0:00) — `slides/01.png`

Let's solve Merge Sorted Arrays, a very hard heaps problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Merge k sorted lists into one sorted list using a min-heap of (value, list, index).

## 3. Intuition (0:19) — `slides/03.png`

A min-heap holds the head of each list; popping it always gives the next smallest overall.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, push each list's first element. Second, pop the min and append. Third, push the next from that list. Fourth, repeat.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with merge sorted arrays. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n log k. Space is O of n plus k.

## 7. Recap (0:50) — `slides/07.png`

To recap Merge Sorted Arrays: A min-heap holds the head of each list; popping it always gives the next smallest overall. Try re-implementing it from scratch without looking.
