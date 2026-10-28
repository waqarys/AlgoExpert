# AlgoExpert · Palindrome Partitioning Min Cuts

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Palindrome Partitioning Min Cuts (0:00) — `slides/01.png`

Let's solve Palindrome Partitioning Min Cuts, a very hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:13) — `slides/02.png`

Here's the problem. Fewest cuts so every piece is a palindrome.

## 3. Intuition (0:18) — `slides/03.png`

Precompute which substrings are palindromes, then fewest cuts for each prefix.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Trying every partition is exponential. A palindrome table plus a min-cuts DP is quadratic.

## 5. Approach (0:32) — `slides/05.png`

Step by step. First, palindrome table by expanding lengths. Second, cuts of i is zero if the prefix is a palindrome. Third, otherwise min over j of cuts plus one.

## 6. Worked example (0:45) — `slides/06.png`

For each end j, consider every palindrome ending there; the cuts are one more than the best for the prefix before it.

## 7. Worked example (0:52) — `slides/07.png`

The minimum is 2 cuts.

## 8. Java solution (0:55) — `slides/08.png`

For each end j, cuts starts at j; for each start i where s i to j is a palindrome, mark it and update cuts j with zero or cuts i minus one plus one.

## 9. Complexity (1:04) — `slides/09.png`

Time is O of n squared. Space is O of n squared.

## 10. Edge cases & pitfalls (1:10) — `slides/10.png`

If the whole string is a palindrome, zero cuts.

## 11. Interview tips & follow-ups (1:14) — `slides/11.png`

Centre expansion avoids the table.

## 12. Recap (1:17) — `slides/12.png`

To recap Palindrome Partitioning Min Cuts: Precompute which substrings are palindromes, then fewest cuts for each prefix. Try re-implementing it from scratch without looking.
