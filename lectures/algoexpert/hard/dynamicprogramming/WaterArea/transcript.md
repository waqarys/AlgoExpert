# AlgoExpert · Water Area

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Water Area (0:00) — `slides/01.png`

Let's solve Water Area, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Pillars of given heights; how much rain water is trapped? Two pointers.

## 3. Intuition (0:19) — `slides/03.png`

Water above a pillar is limited by the smaller of the tallest walls on its left and right.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Scanning both sides for every index is quadratic. Prefix and suffix max arrays make it linear. Two pointers do it in constant space: the lower side's max is the binding limit.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, pointers at both ends with running maxes. Second, move the side with the smaller max. Third, add max minus height. Fourth, continue until they meet.

## 6. Worked example (0:51) — `slides/06.png`

The left side is lower, so its max bounds the water at index 0: 0 units. Total 0.

## 7. Worked example (0:59) — `slides/07.png`

The right side is lower, so its max bounds the water at index 12: 3 units. Total 3.

## 8. Worked example (1:07) — `slides/08.png`

The right side is lower, so its max bounds the water at index 10: 2 units. Total 7.

## 9. Worked example (1:14) — `slides/09.png`

The left side is lower, so its max bounds the water at index 1: 0 units. Total 13.

## 10. Worked example (1:22) — `slides/10.png`

The left side is lower, so its max bounds the water at index 4: 3 units. Total 32.

## 11. Worked example (1:30) — `slides/11.png`

The left side is lower, so its max bounds the water at index 6: 8 units. Total 48.

## 12. Java solution (1:38) — `slides/12.png`

While l is less than r, move the smaller side: update its max, add max minus height, and step inward.

## 13. Complexity (1:44) — `slides/13.png`

Time is O of n. Space is constant.

## 14. Edge cases & pitfalls (1:48) — `slides/14.png`

Always move the side with the smaller height; its max is the limit.

## 15. Interview tips & follow-ups (1:53) — `slides/15.png`

This is trapping rain water.

## 16. Recap (1:56) — `slides/16.png`

To recap Water Area: Water above a pillar is limited by the smaller of the tallest walls on its left and right. Try re-implementing it from scratch without looking.
