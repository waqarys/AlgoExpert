# AlgoExpert · Count Inversions

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Count Inversions (0:00) — `slides/01.png`

Let's solve Count Inversions, a very hard sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Number of pairs i under j with a i over a j , counted during merge sort.

## 3. Intuition (0:18) — `slides/03.png`

Merge sort counts inversions: when a right element is placed before remaining left elements, they all form inversions.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, sort halves recursively. Second, during merge, add remaining left count when taking from the right. Third, sum.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with count inversions. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n log n. Space is O of n.

## 7. Recap (0:48) — `slides/07.png`

To recap Count Inversions: Merge sort counts inversions: when a right element is placed before remaining left elements, they all form inversions. Try re-implementing it from scratch without looking.
