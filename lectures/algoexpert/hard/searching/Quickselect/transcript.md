# AlgoExpert · Quickselect

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Quickselect (0:00) — `slides/01.png`

Let's solve Quickselect, a hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Kth smallest element (1-based) of an unsorted array, in place with Hoare-style partitioning.

## 3. Intuition (0:19) — `slides/03.png`

Partition like quicksort, but only recurse into the side containing the kth position.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, pick a pivot and partition. Second, if the pivot lands at k minus one, done. Third, else continue on one side.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with quickselect. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n avg, O of n squared worst. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Quickselect: Partition like quicksort, but only recurse into the side containing the kth position. Try re-implementing it from scratch without looking.
