# AlgoExpert · Laptop Rentals

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Laptop Rentals (0:00) — `slides/01.png`

Let's solve Laptop Rentals, a hard heaps problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Given start, end) rental intervals, minimum number of laptops needed so nobody waits.

## 3. Intuition (0:19) — `slides/03.png`

The number of laptops needed equals the maximum number of overlapping rentals.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, sort starts and ends separately. Second, sweep with two pointers. Third, a start before the next end needs a laptop. Fourth, otherwise reuse one.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with laptop rentals. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n log n. Space is O of n.

## 7. Recap (0:50) — `slides/07.png`

To recap Laptop Rentals: The number of laptops needed equals the maximum number of overlapping rentals. Try re-implementing it from scratch without looking.
