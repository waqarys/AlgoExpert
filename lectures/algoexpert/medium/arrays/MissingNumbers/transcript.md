# AlgoExpert · Missing Numbers

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Missing Numbers (0:00) — `slides/01.png`

Let's solve Missing Numbers, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Array holds 1..n plus 2 with two numbers missing; return them ascending. Split by the average of the two missing values and sum each half.

## 3. Intuition (0:22) — `slides/03.png`

The numbers one to n plus two sum to a known total; the missing pair splits around their average.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Checking each candidate against the array is quadratic. A hash set makes it linear with extra space. Using sums, we can get constant space: the total tells us the missing pair's sum, and splitting at the average separates them.

## 5. Approach (0:42) — `slides/05.png`

Step by step. First, compute the missing sum. Second, split at the average. Third, sum the expected and actual values below it. Fourth, the difference gives one number, the rest gives the other.

## 6. Worked example (0:58) — `slides/06.png`

With three numbers given, n is five. One through five sums to fifteen, the input sums to 8, so the two missing numbers add up to 7.

## 7. Worked example (1:07) — `slides/07.png`

The two missing numbers are different, so one is at most the average, 3, and the other is above it.

## 8. Worked example (1:14) — `slides/08.png`

The numbers one to 3 should sum to 6; the inputs at most 3 sum to 4. The difference, 2, is the first missing number.

## 9. Worked example (1:23) — `slides/09.png`

The second is 7 minus 2, which is 5. So the answer is 2 and 5.

## 10. Java solution (1:29) — `slides/10.png`

We compute n as length plus two, subtract every input from the expected total to get the missing sum, split it at the average, and compare the expected and actual sums of the lower half to find the first number. The second is the total minus the first.

## 11. Complexity (1:44) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:48) — `slides/12.png`

Use a long for the sums. The missing numbers might be the very first or last, and an empty input means the answer is one and two.

## 13. Interview tips & follow-ups (1:57) — `slides/13.png`

The XOR version works the same way, splitting on a set bit. For k missing numbers, a cyclic sort or bitset generalises.

## 14. Recap (2:06) — `slides/14.png`

To recap Missing Numbers: The numbers one to n plus two sum to a known total; the missing pair splits around their average. Try re-implementing it from scratch without looking.
