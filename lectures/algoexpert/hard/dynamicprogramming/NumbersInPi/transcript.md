# AlgoExpert · Numbers In Pi

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Numbers In Pi (0:00) — `slides/01.png`

Let's solve Numbers In Pi, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Minimum spaces to split the digit string into numbers all from the given list, or -1. DP over suffixes.

## 3. Intuition (0:22) — `slides/03.png`

Find the fewest pieces to cover each suffix of the digits with favourite numbers, using memoisation.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, put numbers in a set. Second, from each start, try every prefix in the set. Third, recurse on the rest with memo. Fourth, spaces equal pieces minus one.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with numbers in pi. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n cubed plus m. Space is O of n plus m.

## 7. Recap (0:55) — `slides/07.png`

To recap Numbers In Pi: Find the fewest pieces to cover each suffix of the digits with favourite numbers, using memoisation. Try re-implementing it from scratch without looking.
