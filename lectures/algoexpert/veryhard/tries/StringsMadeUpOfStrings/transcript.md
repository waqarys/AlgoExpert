# AlgoExpert · Strings Made Up Of Strings

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Strings Made Up Of Strings (0:00) — `slides/01.png`

Let's solve Strings Made Up Of Strings, a very hard tries problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Return the strings from strings that can be built by concatenating two or more strings from substrings (reuse allowed). Word-break DP per string.

## 3. Intuition (0:23) — `slides/03.png`

A trie of the substrings and memoised splitting determine whether a string decomposes into two or more pieces.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

Trying every split is exponential. A word-break DP per string is quadratic in its length.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, build a trie of substrings. Second, from each index, walk the trie for word ends. Third, recurse on the rest with memo. Fourth, require at least two pieces.

## 6. Worked example (0:52) — `slides/06.png`

Which strings can be built from at least two of the substrings?

## 7. Worked example (0:56) — `slides/07.png`

For each string, a word-break DP finds whether it splits into dictionary pieces, and how many.

## 8. Worked example (1:03) — `slides/08.png`

Strings with at least two pieces qualify.

## 9. Java solution (1:06) — `slides/09.png`

For each string we fill pieces from zero, extending when a dictionary substring ends at j, and keep strings with at least two pieces.

## 10. Complexity (1:14) — `slides/10.png`

Time is O of n times m squared. Space is O of m plus s.

## 11. Edge cases & pitfalls (1:20) — `slides/11.png`

A string equal to a single substring doesn't count.

## 12. Interview tips & follow-ups (1:24) — `slides/12.png`

This resembles concatenated words.

## 13. Recap (1:28) — `slides/13.png`

To recap Strings Made Up Of Strings: A trie of the substrings and memoised splitting determine whether a string decomposes into two or more pieces. Try re-implementing it from scratch without looking.
