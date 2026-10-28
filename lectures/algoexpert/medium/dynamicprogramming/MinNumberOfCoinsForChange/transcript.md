# AlgoExpert · Min Number Of Coins For Change

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Number Of Coins For Change (0:00) — `slides/01.png`

Let's solve Min Number Of Coins For Change, a medium dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Fewest coins summing to n, or -1 if impossible.

## 3. Intuition (0:19) — `slides/03.png`

Build the fewest coins for every amount from zero up to n.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Greedy, always taking the biggest coin, fails for coins like one, three and four with six: greedy gives four, one, one, but three plus three is better. Recursion explores exponentially many choices. A bottom-up table over amounts takes n times the number of coins.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, array of infinities, zero for amount zero. Second, for each coin, relax amounts from the coin up. Third, answer or minus one.

## 6. Worked example (0:53) — `slides/06.png`

Processing coin 1: each amount from 1 up tries using one 1-coin plus the best for the remainder. Now seven needs 7 coins.

## 7. Worked example (1:02) — `slides/07.png`

Processing coin 5: each amount from 5 up tries using one 5-coin plus the best for the remainder. Now seven needs 3 coins.

## 8. Worked example (1:11) — `slides/08.png`

Coin 10 is bigger than 7, so it can't help.

## 9. Java solution (1:15) — `slides/09.png`

We fill dp with max value and set dp of zero to zero. For each coin, for each amount from the coin up, if the remainder is reachable we take the min with one more coin. Finally we map max value to minus one.

## 10. Complexity (1:30) — `slides/10.png`

Time is O of n times d. Space is O of n.

## 11. Edge cases & pitfalls (1:34) — `slides/11.png`

Zero needs zero coins, unreachable amounts return minus one, and you must check for infinity before adding one, to avoid overflow.

## 12. Interview tips & follow-ups (1:42) — `slides/12.png`

Show the greedy counterexample early. A follow-up returns the coins themselves by storing the last coin used per amount.

## 13. Recap (1:51) — `slides/13.png`

To recap Min Number Of Coins For Change: Build the fewest coins for every amount from zero up to n. Try re-implementing it from scratch without looking.
