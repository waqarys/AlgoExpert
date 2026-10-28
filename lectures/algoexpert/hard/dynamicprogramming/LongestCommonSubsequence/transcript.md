# AlgoExpert · Longest Common Subsequence

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Common Subsequence (0:00) — `slides/01.png`

Let's solve Longest Common Subsequence, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. One LCS of two strings as a list of chars.

## 3. Intuition (0:18) — `slides/03.png`

Match characters along two prefixes: a match extends the diagonal, otherwise take the better of dropping one character.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Enumerating subsequences is exponential. A DP over prefixes is n times m, and backtracking recovers the actual letters.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, build the LCS length table. Second, equal characters add one to the diagonal. Third, otherwise take the max of top or left. Fourth, backtrack to recover the letters.

## 6. Worked example (0:51) — `slides/06.png`

Fill the table: matching letters take the diagonal plus one; otherwise the max of above and left. Green cells are matches.

## 7. Worked example (0:59) — `slides/07.png`

Backtrack from the bottom-right: on a match, take the letter and go diagonally; otherwise move toward the larger neighbour.

## 8. Worked example (1:06) — `slides/08.png`

The longest common subsequence is X, Y, Z, W, length 4.

## 9. Java solution (1:12) — `slides/09.png`

We fill the table with the match-or-max rule, then walk back from n, m, prepending matching characters.

## 10. Complexity (1:19) — `slides/10.png`

Time is O of n times m. Space is O of n times m.

## 11. Edge cases & pitfalls (1:23) — `slides/11.png`

Mind the padding row and column. Ties during backtracking can go either way.

## 12. Interview tips & follow-ups (1:29) — `slides/12.png`

Relate it to diff tools and edit distance.

## 13. Recap (1:33) — `slides/13.png`

To recap Longest Common Subsequence: Match characters along two prefixes: a match extends the diagonal, otherwise take the better of dropping one character. Try re-implementing it from scratch without looking.
