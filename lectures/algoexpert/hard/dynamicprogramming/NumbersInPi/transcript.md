# AlgoExpert · Numbers In Pi

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Numbers In Pi (0:00) — `slides/01.png`

Let's solve Numbers In Pi, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Minimum spaces to split the digit string into numbers all from the given list, or -1. DP over suffixes.

## 3. Intuition (0:22) — `slides/03.png`

Find the fewest pieces to cover each suffix of the digits with favourite numbers, using memoisation.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Trying every split is exponential. A DP over suffixes, the fewest spaces from index i onward, is quadratic with a hash set of numbers.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, put numbers in a set. Second, from each start, try every prefix in the set. Third, recurse on the rest with memo. Fourth, spaces equal pieces minus one.

## 6. Worked example (0:53) — `slides/06.png`

From index 6, try every favourite number starting here: the fewest spaces for the rest is 0.

## 7. Worked example (1:00) — `slides/07.png`

From index 5, try every favourite number starting here: the fewest spaces for the rest is 1.

## 8. Worked example (1:06) — `slides/08.png`

From index 4, try every favourite number starting here: the fewest spaces for the rest is 2.

## 9. Worked example (1:13) — `slides/09.png`

From index 2, try every favourite number starting here: the fewest spaces for the rest is 1.

## 10. Worked example (1:19) — `slides/10.png`

From index 0, try every favourite number starting here: the fewest spaces for the rest is 2.

## 11. Java solution (1:26) — `slides/11.png`

Dp of n is minus one. From the end backward, for each j, if the rest is solvable and pi from i to j is a favourite, take dp j plus one. Return dp zero or minus one.

## 12. Complexity (1:39) — `slides/12.png`

Time is O of n cubed plus m. Space is O of n plus m.

## 13. Edge cases & pitfalls (1:44) — `slides/13.png`

Seed the end with minus one, because there's no space after the last number.

## 14. Interview tips & follow-ups (1:49) — `slides/14.png`

This is word break, minimising the pieces.

## 15. Recap (1:53) — `slides/15.png`

To recap Numbers In Pi: Find the fewest pieces to cover each suffix of the digits with favourite numbers, using memoisation. Try re-implementing it from scratch without looking.
