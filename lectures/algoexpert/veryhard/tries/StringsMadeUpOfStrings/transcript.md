# AlgoExpert · Strings Made Up Of Strings

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Strings Made Up Of Strings (0:00) — `slides/01.png`

Let's solve Strings Made Up Of Strings, a very hard tries problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Return the strings from strings that can be built by concatenating two or more strings from substrings (reuse allowed). Word-break DP per string.

## 3. Intuition (0:23) — `slides/03.png`

A trie of the substrings and memoised splitting determine whether a string decomposes into two or more pieces.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, build a trie of substrings. Second, from each index, walk the trie for word ends. Third, recurse on the rest with memo. Fourth, require at least two pieces.

## 5. Java solution (0:45) — `slides/05.png`

Here's the Java solution, starting with strings made up of strings. It follows the steps we just described.

## 6. Complexity (0:52) — `slides/06.png`

Time is O of n times m squared. Space is O of m plus s.

## 7. Recap (0:58) — `slides/07.png`

To recap Strings Made Up Of Strings: A trie of the substrings and memoised splitting determine whether a string decomposes into two or more pieces. Try re-implementing it from scratch without looking.
