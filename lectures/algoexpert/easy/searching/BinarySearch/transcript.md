# AlgoExpert · Binary Search

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Binary Search (0:00) — `slides/01.png`

Let's solve Binary Search, an easy searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return the index of target in a sorted array, or -1.

## 3. Intuition (0:18) — `slides/03.png`

In a sorted array, comparing with the middle element tells us which half can contain the target.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

A linear scan checks every element. Binary search halves the remaining range with each comparison, so a million items need only about twenty steps.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, keep left and right bounds. Second, check the middle. Third, discard the half that can't contain the target. Fourth, return the index or minus one.

## 6. Worked example (0:48) — `slides/06.png`

The middle is index 4 with value 45, which is larger than 33, so we discard the right half.

## 7. Worked example (0:55) — `slides/07.png`

The middle is index 1 with value 1, which is smaller than 33, so we discard the left half.

## 8. Worked example (1:02) — `slides/08.png`

The middle is index 2 with value 21, which is smaller than 33, so we discard the left half.

## 9. Worked example (1:09) — `slides/09.png`

The middle value is 33. Found it at index 3.

## 10. Java solution (1:14) — `slides/10.png`

We keep left and right. While left is at most right, compute mid. Return mid on a match, otherwise move left past mid or right before it. Return minus one at the end.

## 11. Complexity (1:26) — `slides/11.png`

Time is O of log n. Space is constant.

## 12. Edge cases & pitfalls (1:30) — `slides/12.png`

Use left less than or equal to right, compute mid without overflow, and return minus one if not found.

## 13. Interview tips & follow-ups (1:37) — `slides/13.png`

Know both versions. Variations like first occurrence, rotated arrays, and binary search on the answer appear constantly.

## 14. Recap (1:45) — `slides/14.png`

To recap Binary Search: In a sorted array, comparing with the middle element tells us which half can contain the target. Try re-implementing it from scratch without looking.
