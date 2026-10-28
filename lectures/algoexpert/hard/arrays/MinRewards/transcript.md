# AlgoExpert · Min Rewards

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Rewards (0:00) — `slides/01.png`

Let's solve Min Rewards, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Each student gets over equals 1 reward; a student scoring higher than an adjacent one gets more. Minimum total. Two passes (left-to-right, right-to-left).

## 3. Intuition (0:24) — `slides/03.png`

Each student must beat a lower-scoring neighbour on both sides, so do one pass each way and take the max.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, everyone starts with one. Second, left to right, give one more than a lower left neighbour. Third, right to left, ensure one more than a lower right neighbour. Fourth, sum the rewards.

## 5. Java solution (0:47) — `slides/05.png`

Here's the Java solution, starting with min rewards. It follows the steps we just described.

## 6. Complexity (0:54) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:57) — `slides/07.png`

To recap Min Rewards: Each student must beat a lower-scoring neighbour on both sides, so do one pass each way and take the max. Try re-implementing it from scratch without looking.
