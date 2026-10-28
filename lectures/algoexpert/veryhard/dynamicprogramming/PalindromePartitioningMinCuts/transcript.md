# AlgoExpert · Palindrome Partitioning Min Cuts

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Palindrome Partitioning Min Cuts (0:00) — `slides/01.png`

Let's solve Palindrome Partitioning Min Cuts, a very hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:13) — `slides/02.png`

Here's the problem. Fewest cuts so every piece is a palindrome.

## 3. Intuition (0:18) — `slides/03.png`

Precompute which substrings are palindromes, then fewest cuts for each prefix.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, palindrome table by expanding lengths. Second, cuts of i is zero if the prefix is a palindrome. Third, otherwise min over j of cuts plus one.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with palindrome partitioning min cuts. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n squared. Space is O of n squared.

## 7. Recap (0:51) — `slides/07.png`

To recap Palindrome Partitioning Min Cuts: Precompute which substrings are palindromes, then fewest cuts for each prefix. Try re-implementing it from scratch without looking.
