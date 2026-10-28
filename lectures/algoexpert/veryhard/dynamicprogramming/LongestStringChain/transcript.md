# AlgoExpert · Longest String Chain

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest String Chain (0:00) — `slides/01.png`

Let's solve Longest String Chain, a very hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. A chain is built by removing one character at a time where every intermediate string is in the input. Return the longest chain (length over equals 2) from longest to shortest, or .

## 3. Intuition (0:25) — `slides/03.png`

Process strings by length; each string's chain extends the best chain of any one-character-shorter string.

## 4. Brute force vs optimal (0:32) — `slides/04.png`

Comparing every pair is quadratic in the number of strings. Sorting by length and trying each single deletion with a hash map is n times L squared.

## 5. Approach (0:41) — `slides/05.png`

Step by step. First, sort by length. Second, for each string, try removing each character. Third, look up the result. Fourth, keep best lengths and next links.

## 6. Worked example (0:55) — `slides/06.png`

Sort by length. For each string, delete each character in turn; if the shorter string exists, extend its chain.

## 7. Worked example (1:03) — `slides/07.png`

The longest chain is abcdef, abcde, abde, ade, ae.

## 8. Java solution (1:09) — `slides/08.png`

We sort by length; each string starts at length one, and for each deletion that exists we extend and remember the link. Then we follow links from the best start.

## 9. Complexity (1:19) — `slides/09.png`

Time is O of n times m squared plus n log n. Space is O of n times m.

## 10. Edge cases & pitfalls (1:24) — `slides/10.png`

A single string isn't a chain; return empty if the best is one.

## 11. Interview tips & follow-ups (1:29) — `slides/11.png`

It's longest increasing subsequence on a different relation.

## 12. Recap (1:34) — `slides/12.png`

To recap Longest String Chain: Process strings by length; each string's chain extends the best chain of any one-character-shorter string. Try re-implementing it from scratch without looking.
