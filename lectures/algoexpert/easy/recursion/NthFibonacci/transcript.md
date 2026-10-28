# AlgoExpert · Nth Fibonacci

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Nth Fibonacci (0:00) — `slides/01.png`

Let's solve Nth Fibonacci, an easy recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. F(1) equals 0, F(2) equals 1. Iterative with two variables.

## 3. Intuition (0:20) — `slides/03.png`

Each number only depends on the previous two, so we don't need recursion or an array.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, handle n of one and two. Second, keep the last two values. Third, slide them forward n minus two times. Fourth, return the latest.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with get nth fib. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Nth Fibonacci: Each number only depends on the previous two, so we don't need recursion or an array. Try re-implementing it from scratch without looking.
