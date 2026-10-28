# AlgoExpert · Longest Common Subsequence

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Common Subsequence (0:00) — `slides/01.png`

Let's solve Longest Common Subsequence, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. One LCS of two strings as a list of chars.

## 3. Intuition (0:18) — `slides/03.png`

Match characters along two prefixes: a match extends the diagonal, otherwise take the better of dropping one character.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, build the LCS length table. Second, equal characters add one to the diagonal. Third, otherwise take the max of top or left. Fourth, backtrack to recover the letters.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with longest common subsequence. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n times m. Space is O of n times m.

## 7. Recap (0:53) — `slides/07.png`

To recap Longest Common Subsequence: Match characters along two prefixes: a match extends the diagonal, otherwise take the better of dropping one character. Try re-implementing it from scratch without looking.
