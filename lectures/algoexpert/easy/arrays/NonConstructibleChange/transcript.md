# AlgoExpert · Non Constructible Change

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Non Constructible Change (0:00) — `slides/01.png`

Let's solve Non Constructible Change, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Given positive coin values, find the minimum amount that cannot be formed. Sort; if the next coin exceeds (reachable plus 1), reachable plus 1 is the answer.

## 3. Intuition (0:24) — `slides/03.png`

Sort the coins. If you can already build every amount up to some total, a coin bigger than total plus one leaves a gap you can never fill.

## 4. Brute force vs optimal (0:33) — `slides/04.png`

The brute-force idea is to test amounts one, two, three and so on, checking each against every subset of coins. That's exponential. Sorting first lets a single greedy pass track the largest reachable amount, so the whole thing is n log n.

## 5. Approach (0:48) — `slides/05.png`

Step by step. First, sort the coins ascending. Second, track change, the largest amount you can build so far. Third, if a coin exceeds change plus one, return change plus one. Fourth, otherwise add the coin to change.

## 6. Worked example (1:05) — `slides/06.png`

Let's use the coins five, seven, one, one, two, three and twenty-two. After sorting, we start with change equal to zero.

## 7. Worked example (1:15) — `slides/07.png`

Coin 1 is at most 0 plus one, so it extends our reach: every amount up to 1 can be made.

## 8. Worked example (1:21) — `slides/08.png`

Coin 2 is at most 2 plus one, so it extends our reach: every amount up to 4 can be made.

## 9. Worked example (1:27) — `slides/09.png`

Coin 3 is at most 4 plus one, so it extends our reach: every amount up to 7 can be made.

## 10. Worked example (1:33) — `slides/10.png`

Coin 5 is at most 7 plus one, so it extends our reach: every amount up to 12 can be made.

## 11. Worked example (1:40) — `slides/11.png`

Now coin 22 is bigger than 19 plus one. There's no way to make 20, so that's our answer.

## 12. Java solution (1:47) — `slides/12.png`

The whole solution is a few lines. We sort the array, keep a running total called reach, and for each coin break out as soon as the coin exceeds reach plus one. Otherwise we add it. Whatever reach plus one is at the end is the answer.

## 13. Complexity (2:03) — `slides/13.png`

Time is O of n log n. Space is constant (in-place sort).

## 14. Edge cases & pitfalls (2:07) — `slides/14.png`

Edge cases: with no coins the answer is one. Duplicates are fine. The invariant only holds if coins are processed in ascending order, so forgetting to sort is the classic bug. And with big values, use a long for the running total.

## 15. Interview tips & follow-ups (2:23) — `slides/15.png`

In the interview, state the invariant clearly: every amount from one to change is buildable. That's an induction proof. A good follow-up is what changes if coins can be reused.

## 16. Recap (2:35) — `slides/16.png`

To recap Non Constructible Change: Sort the coins. If you can already build every amount up to some total, a coin bigger than total plus one leaves a gap you can never fill. Try re-implementing it from scratch without looking.
