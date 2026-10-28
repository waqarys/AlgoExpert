# AlgoExpert · Apartment Hunting

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Apartment Hunting (0:00) — `slides/01.png`

Let's solve Apartment Hunting, a very hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Blocks list which buildings (reqs) they contain. Choose the block minimising the farthest distance you'd walk to reach any required building. Precompute nearest distance per req with a left and right sweep.

## 3. Intuition (0:26) — `slides/03.png`

For each requirement, precompute the distance from every block to its nearest building, with a left and a right sweep.

## 4. Approach (0:33) — `slides/04.png`

Step by step. First, for each requirement, sweep left to right and right to left. Second, store min distances. Third, for each block, take the max over requirements. Fourth, pick the block with the smallest max.

## 5. Java solution (0:50) — `slides/05.png`

Here's the Java solution, starting with apartment hunting. It follows the steps we just described.

## 6. Complexity (0:57) — `slides/06.png`

Time is O of b times r. Space is O of b times r.

## 7. Recap (1:02) — `slides/07.png`

To recap Apartment Hunting: For each requirement, precompute the distance from every block to its nearest building, with a left and a right sweep. Try re-implementing it from scratch without looking.
