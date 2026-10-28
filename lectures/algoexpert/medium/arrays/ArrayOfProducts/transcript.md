# AlgoExpert · Array Of Products

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Array Of Products (0:00) — `slides/01.png`

Let's solve Array Of Products, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Out i equals product of every element except a i , without division. Prefix products then suffix products.

## 3. Intuition (0:21) — `slides/03.png`

Each output is the product of everything to the left times everything to the right, so two sweeps replace division.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, fill each slot with the running product from the left. Second, sweep from the right with a second running product. Third, multiply it in. Fourth, no division needed.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with array of products. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n. Space is O of n output.

## 7. Recap (0:53) — `slides/07.png`

To recap Array Of Products: Each output is the product of everything to the left times everything to the right, so two sweeps replace division. Try re-implementing it from scratch without looking.
