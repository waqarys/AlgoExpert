# AlgoExpert · Sort K Sorted Array

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sort K Sorted Array (0:00) — `slides/01.png`

Let's solve Sort K Sorted Array, a hard heaps problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Every element is at most k positions from its sorted position; sort with a size-(k plus 1) min-heap.

## 3. Intuition (0:20) — `slides/03.png`

Every element is within k of its spot, so the minimum of the next k plus one items is always next in order.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, fill a min-heap with k plus one items. Second, pop the min into place. Third, push the next item. Fourth, drain the heap.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with sort k sorted array. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of n log k. Space is O of k.

## 7. Recap (0:52) — `slides/07.png`

To recap Sort K Sorted Array: Every element is within k of its spot, so the minimum of the next k plus one items is always next in order. Try re-implementing it from scratch without looking.
