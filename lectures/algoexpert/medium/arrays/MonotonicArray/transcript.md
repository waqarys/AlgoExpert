# AlgoExpert · Monotonic Array

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Monotonic Array (0:00) — `slides/01.png`

Let's solve Monotonic Array, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Is the array entirely non-increasing or entirely non-decreasing?

## 3. Intuition (0:18) — `slides/03.png`

An array is monotonic if it never goes both up and down.

## 4. Approach (0:22) — `slides/04.png`

Step by step. First, track two flags, non-increasing and non-decreasing. Second, clear the opposite flag on each rise or fall. Third, return true if either flag survives.

## 5. Java solution (0:32) — `slides/05.png`

Here's the Java solution, starting with is monotonic. It follows the steps we just described.

## 6. Complexity (0:39) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:43) — `slides/07.png`

To recap Monotonic Array: An array is monotonic if it never goes both up and down. Try re-implementing it from scratch without looking.
