# AlgoExpert · Radix Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Radix Sort (0:00) — `slides/01.png`

Let's solve Radix Sort, a hard sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sort non-negative ints by LSD radix sort with counting sort per decimal digit.

## 3. Intuition (0:19) — `slides/03.png`

Sort by each decimal digit from least significant, using a stable counting sort each time.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, find the max to know digit count. Second, for each digit, count, prefix sum, and place stably. Third, copy back.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with radix sort. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of d times (n plus 10). Space is O of n.

## 7. Recap (0:50) — `slides/07.png`

To recap Radix Sort: Sort by each decimal digit from least significant, using a stable counting sort each time. Try re-implementing it from scratch without looking.
