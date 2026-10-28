# AlgoExpert · Missing Numbers

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Missing Numbers (0:00) — `slides/01.png`

Let's solve Missing Numbers, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Array holds 1..n plus 2 with two numbers missing; return them ascending. Split by the average of the two missing values and sum each half.

## 3. Intuition (0:22) — `slides/03.png`

The numbers one to n plus two sum to a known total; the missing pair splits around their average.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, compute the missing sum. Second, split at the average. Third, sum the expected and actual values below it. Fourth, the difference gives one number, the rest gives the other.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with missing numbers. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:54) — `slides/07.png`

To recap Missing Numbers: The numbers one to n plus two sum to a known total; the missing pair splits around their average. Try re-implementing it from scratch without looking.
