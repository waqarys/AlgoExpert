# AlgoExpert · Smallest Difference

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Smallest Difference (0:00) — `slides/01.png`

Let's solve Smallest Difference, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Pick one number from each array with the smallest absolute difference; return a, b .

## 3. Intuition (0:19) — `slides/03.png`

Sort both arrays, then walk them together, always advancing the smaller value to close the gap.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Checking every pair costs n times m. After sorting both arrays, two pointers walk forward, always advancing the smaller value, because moving the larger one can only make the difference bigger.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, sort both. Second, compare current values and record the gap. Third, advance the pointer at the smaller value. Fourth, stop early on zero.

## 6. Worked example (0:51) — `slides/06.png`

Comparing -1 and 15: difference 16. The best so far is -1 and 15. We advance the pointer at the smaller value to close the gap.

## 7. Worked example (1:02) — `slides/07.png`

Comparing 5 and 15: difference 10. The best so far is 5 and 15. We advance the pointer at the smaller value to close the gap.

## 8. Worked example (1:13) — `slides/08.png`

Comparing 10 and 15: difference 5. The best so far is 10 and 15. We advance the pointer at the smaller value to close the gap.

## 9. Worked example (1:23) — `slides/09.png`

Comparing 20 and 17: difference 3. The best so far is 20 and 17. We advance the pointer at the smaller value to close the gap.

## 10. Worked example (1:34) — `slides/10.png`

Comparing 20 and 26: difference 6. The best so far is 20 and 17. We advance the pointer at the smaller value to close the gap.

## 11. Worked example (1:45) — `slides/11.png`

Comparing 28 and 134: difference 106. The best so far is 28 and 26. We advance the pointer at the smaller value to close the gap.

## 12. Java solution (1:58) — `slides/12.png`

We sort both arrays, then loop while both pointers are in range. We compute the absolute difference as a long, keep the best pair, and advance whichever side is smaller, breaking on an exact match.

## 13. Complexity (2:10) — `slides/13.png`

Time is O of n log n plus m log m. Space is constant.

## 14. Edge cases & pitfalls (2:15) — `slides/14.png`

If the values are equal, the difference is zero and we can stop. Use a long for the subtraction to avoid overflow.

## 15. Interview tips & follow-ups (2:23) — `slides/15.png`

Explain clearly why moving the smaller pointer never misses the answer.

## 16. Recap (2:28) — `slides/16.png`

To recap Smallest Difference: Sort both arrays, then walk them together, always advancing the smaller value to close the gap. Try re-implementing it from scratch without looking.
