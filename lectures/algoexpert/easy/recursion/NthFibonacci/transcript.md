# AlgoExpert · Nth Fibonacci

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Nth Fibonacci (0:00) — `slides/01.png`

Let's solve Nth Fibonacci, an easy recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. F(1) equals 0, F(2) equals 1. Iterative with two variables.

## 3. Intuition (0:20) — `slides/03.png`

Each number only depends on the previous two, so we don't need recursion or an array.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Naive recursion recomputes the same values exponentially many times. Memoising fixes that with linear space. The best version just keeps the last two numbers and slides forward.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, handle n of one and two. Second, keep the last two values. Third, slide them forward n minus two times. Fourth, return the latest.

## 6. Worked example (0:53) — `slides/06.png`

To get F 3, add the last two values: 0 plus 1 equals 1. Then slide the window forward.

## 7. Worked example (1:01) — `slides/07.png`

To get F 4, add the last two values: 1 plus 1 equals 2. Then slide the window forward.

## 8. Worked example (1:08) — `slides/08.png`

To get F 5, add the last two values: 1 plus 2 equals 3. Then slide the window forward.

## 9. Worked example (1:16) — `slides/09.png`

To get F 6, add the last two values: 2 plus 3 equals 5. Then slide the window forward.

## 10. Worked example (1:24) — `slides/10.png`

To get F 7, add the last two values: 3 plus 5 equals 8. Then slide the window forward.

## 11. Java solution (1:32) — `slides/11.png`

We return zero and one for the base cases. Otherwise we keep two variables and loop n minus two times, replacing them with the next pair.

## 12. Complexity (1:41) — `slides/12.png`

Time is O of n. Space is constant.

## 13. Edge cases & pitfalls (1:45) — `slides/13.png`

Note this problem's indexing: the first Fibonacci number is zero and the second is one. For large n, values overflow, so use a long or a big integer.

## 14. Interview tips & follow-ups (1:55) — `slides/14.png`

Draw the recursion tree to explain the exponential blow-up. A strong follow-up is the log n matrix-power method.

## 15. Recap (2:04) — `slides/15.png`

To recap Nth Fibonacci: Each number only depends on the previous two, so we don't need recursion or an array. Try re-implementing it from scratch without looking.
