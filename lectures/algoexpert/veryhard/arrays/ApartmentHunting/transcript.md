# AlgoExpert · Apartment Hunting

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Apartment Hunting (0:00) — `slides/01.png`

Let's solve Apartment Hunting, a very hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Blocks list which buildings (reqs) they contain. Choose the block minimising the farthest distance you'd walk to reach any required building. Precompute nearest distance per req with a left and right sweep.

## 3. Intuition (0:26) — `slides/03.png`

For each requirement, precompute the distance from every block to its nearest building, with a left and a right sweep.

## 4. Brute force vs optimal (0:33) — `slides/04.png`

Scanning outward from every block is quadratic. Two linear sweeps per requirement give nearest distances, so the whole thing is blocks times requirements.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, for each requirement, sweep left to right and right to left. Second, store min distances. Third, for each block, take the max over requirements. Fourth, pick the block with the smallest max.

## 6. Worked example (1:00) — `slides/06.png`

For each requirement, two sweeps, left to right and right to left, give every block's distance to the nearest one.

## 7. Worked example (1:07) — `slides/07.png`

Each block's score is its farthest requirement. The minimum, 1, is at block 3.

## 8. Java solution (1:14) — `slides/08.png`

For each requirement, the forward sweep tracks the last block with it and the backward sweep the next one; each block keeps the min, and worst keeps the max across requirements. Return the index of the smallest worst.

## 9. Complexity (1:27) — `slides/09.png`

Time is O of b times r. Space is O of b times r.

## 10. Edge cases & pitfalls (1:31) — `slides/10.png`

Use large sentinel distances before the first occurrence.

## 11. Interview tips & follow-ups (1:35) — `slides/11.png`

Frame it as minimising the maximum distance.

## 12. Recap (1:39) — `slides/12.png`

To recap Apartment Hunting: For each requirement, precompute the distance from every block to its nearest building, with a left and a right sweep. Try re-implementing it from scratch without looking.
