# AlgoExpert · Two Number Sum

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Two Number Sum (0:00) — `slides/01.png`

Let's solve Two Number Sum, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Given distinct integers and a target, return any pair summing to the target (empty array if none).

## 3. Intuition (0:19) — `slides/03.png`

For each number x, we need to know if its partner, target minus x, has already appeared. A hash set answers that instantly.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

The brute force checks every pair, which is n squared. Sorting and using two pointers gets n log n with constant extra space. The hash-set approach is linear: for each number, we just ask whether its partner has already appeared.

## 5. Approach (0:42) — `slides/05.png`

Step by step. First, walk the array once. Second, check whether target minus x is in the set. Third, if so, return the pair. Fourth, otherwise add x to the set.

## 6. Worked example (0:57) — `slides/06.png`

Let's trace the array three, five, minus four, eight, eleven, one, minus one, six, with a target of ten.

## 7. Worked example (1:05) — `slides/07.png`

At index 0 the value is 3, so we need 7. It isn't in the set yet, so we add 3 and move on.

## 8. Worked example (1:12) — `slides/08.png`

At index 2 the value is -4, so we need 14. It isn't in the set yet, so we add -4 and move on.

## 9. Worked example (1:21) — `slides/09.png`

At index 3 the value is 8, so we need 2. It isn't in the set yet, so we add 8 and move on.

## 10. Worked example (1:28) — `slides/10.png`

At index 4 the value is 11, so we need -1. It isn't in the set yet, so we add 11 and move on.

## 11. Worked example (1:37) — `slides/11.png`

At -1 we need 11, and it's already in the set. We return 11 and -1.

## 12. Java solution (1:44) — `slides/12.png`

We create a hash set, loop over the array, and for each value x check whether target minus x is in the set. If it is, we return the pair right away; otherwise we add x. Falling out of the loop means no pair exists.

## 13. Complexity (1:57) — `slides/13.png`

Time is O of n. Space is O of n using a hash set of seen values.

## 14. Edge cases & pitfalls (2:02) — `slides/14.png`

If there's no pair, return an empty array. Checking the set before adding the current number guarantees we never pair a number with itself.

## 15. Interview tips & follow-ups (2:11) — `slides/15.png`

Walk through all three approaches and their trade-offs. Common follow-ups are returning indices, finding all pairs, or extending to three-number sum.

## 16. Recap (2:21) — `slides/16.png`

To recap Two Number Sum: For each number x, we need to know if its partner, target minus x, has already appeared. A hash set answers that instantly. Try re-implementing it from scratch without looking.
