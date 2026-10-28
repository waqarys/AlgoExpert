# AlgoExpert · Two Number Sum

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Two Number Sum (0:00) — `slides/01.png`

Let's solve Two Number Sum, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Given distinct integers and a target, return any pair summing to the target (empty array if none).

## 3. Intuition (0:19) — `slides/03.png`

For each number x, we need to know if its partner, target minus x, has already appeared. A hash set answers that instantly.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, walk the array once. Second, check whether target minus x is in the set. Third, if so, return the pair. Fourth, otherwise add x to the set.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with two number sum. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n. Space is O of n using a hash set of seen values.

## 7. Recap (0:55) — `slides/07.png`

To recap Two Number Sum: For each number x, we need to know if its partner, target minus x, has already appeared. A hash set answers that instantly. Try re-implementing it from scratch without looking.
