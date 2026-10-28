# AlgoExpert · Longest Subarray With Sum

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Subarray With Sum (0:00) — `slides/01.png`

Let's solve Longest Subarray With Sum, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Non-negative ints; start, end of the longest subarray summing to target, or if none. Sliding window.

## 3. Intuition (0:21) — `slides/03.png`

Values are non-negative, so a sliding window grows to add and shrinks to subtract.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Checking every subarray is quadratic. Since values are non-negative, a sliding window works: grow right, shrink left when the sum is too big, in linear time.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, expand the right edge adding values. Second, shrink from the left while the sum is too big. Third, record the longest window equal to target.

## 6. Worked example (0:50) — `slides/06.png`

Extend to 1; the window sum is 1.

## 7. Worked example (0:54) — `slides/07.png`

Extend to 3; the window sum is 6.

## 8. Worked example (0:58) — `slides/08.png`

Extend to 3; the window sum is 10. Best so far: indices 0 to 3.

## 9. Worked example (1:05) — `slides/09.png`

Extend to 3; the window sum is 10. Best so far: indices 0 to 3.

## 10. Worked example (1:12) — `slides/10.png`

Extend to 2; the window sum is 9. Best so far: indices 0 to 3.

## 11. Worked example (1:19) — `slides/11.png`

Extend to 2; the window sum is 9. Best so far: indices 4 to 8.

## 12. Java solution (1:25) — `slides/12.png`

We grow r, add a r, shrink from l while the sum exceeds target, and record the window when it matches and is longer.

## 13. Complexity (1:33) — `slides/13.png`

Time is O of n. Space is constant.

## 14. Edge cases & pitfalls (1:36) — `slides/14.png`

The window only works because values are non-negative; zeros can extend a match. With negatives, use prefix sums and a hash map.

## 15. Interview tips & follow-ups (1:46) — `slides/15.png`

Mention the prefix-sum and hash-map version for negative numbers.

## 16. Recap (1:50) — `slides/16.png`

To recap Longest Subarray With Sum: Values are non-negative, so a sliding window grows to add and shrinks to subtract. Try re-implementing it from scratch without looking.
