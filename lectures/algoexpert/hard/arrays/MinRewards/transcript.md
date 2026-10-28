# AlgoExpert · Min Rewards

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Rewards (0:00) — `slides/01.png`

Let's solve Min Rewards, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Each student gets over equals 1 reward; a student scoring higher than an adjacent one gets more. Minimum total. Two passes (left-to-right, right-to-left).

## 3. Intuition (0:24) — `slides/03.png`

Each student must beat a lower-scoring neighbour on both sides, so do one pass each way and take the max.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Repeatedly fixing violations is quadratic. Two passes, one for each direction, satisfy left and right constraints in linear time.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, everyone starts with one. Second, left to right, give one more than a lower left neighbour. Third, right to left, ensure one more than a lower right neighbour. Fourth, sum the rewards.

## 6. Worked example (0:56) — `slides/06.png`

Everyone starts with one reward.

## 7. Worked example (0:59) — `slides/07.png`

Left to right: if a student beats their left neighbour, give them one more than that neighbour.

## 8. Worked example (1:05) — `slides/08.png`

Right to left: if a student beats their right neighbour, take the max of what they have and one more than the right neighbour.

## 9. Worked example (1:11) — `slides/09.png`

Summing gives 25 rewards, the minimum that satisfies both neighbours.

## 10. Java solution (1:17) — `slides/10.png`

We fill rewards with one, sweep left giving one more than the left neighbour when higher, sweep right taking the max with right plus one, and sum.

## 11. Complexity (1:25) — `slides/11.png`

Time is O of n. Space is O of n.

## 12. Edge cases & pitfalls (1:29) — `slides/12.png`

In the second pass, take the max, or you'll undo the left pass.

## 13. Interview tips & follow-ups (1:33) — `slides/13.png`

This is the candy problem.

## 14. Recap (1:36) — `slides/14.png`

To recap Min Rewards: Each student must beat a lower-scoring neighbour on both sides, so do one pass each way and take the max. Try re-implementing it from scratch without looking.
