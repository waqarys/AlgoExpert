# AlgoExpert · Kadanes Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Kadanes Algorithm (0:00) — `slides/01.png`

Let's solve Kadanes Algorithm, a medium famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Maximum sum of a non-empty contiguous subarray.

## 3. Intuition (0:18) — `slides/03.png`

The best subarray ending here is either this element alone or it extends the best ending at the previous index.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Summing every subarray is quadratic. Divide and conquer is n log n. Kadane's algorithm keeps the best sum ending at each index: either extend the previous run or start fresh, which is linear with constant space.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, running best ending here. Second, max of element or element plus running. Third, track the global max.

## 6. Worked example (0:49) — `slides/06.png`

At -9: extending the previous run gives -1. The best overall is 8.

## 7. Worked example (0:56) — `slides/07.png`

At 1: starting fresh beats extending, so we restart here. The best overall is 8.

## 8. Worked example (1:03) — `slides/08.png`

At 7: extending the previous run gives 16. The best overall is 16.

## 9. Worked example (1:10) — `slides/09.png`

At 2: extending the previous run gives 18. The best overall is 18.

## 10. Worked example (1:17) — `slides/10.png`

At 1: extending the previous run gives 19. The best overall is 19.

## 11. Worked example (1:24) — `slides/11.png`

At 4: extending the previous run gives 18. The best overall is 19.

## 12. Java solution (1:31) — `slides/12.png`

Cur and best start at the first element. For each next element, cur becomes the max of the element alone or cur plus the element, and best tracks the max of cur.

## 13. Complexity (1:41) — `slides/13.png`

Time is O of n. Space is constant.

## 14. Edge cases & pitfalls (1:45) — `slides/14.png`

If everything is negative, the answer is the largest single element, which is why we initialise with the first element rather than zero.

## 15. Interview tips & follow-ups (1:53) — `slides/15.png`

Follow-ups return the start and end indices, handle circular arrays, or extend to two-dimensional submatrices.

## 16. Recap (2:01) — `slides/16.png`

To recap Kadanes Algorithm: The best subarray ending here is either this element alone or it extends the best ending at the previous index. Try re-implementing it from scratch without looking.
