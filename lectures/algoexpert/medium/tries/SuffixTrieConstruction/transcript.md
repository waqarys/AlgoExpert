# AlgoExpert · Suffix Trie Construction

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Suffix Trie Construction (0:00) — `slides/01.png`

Let's solve Suffix Trie Construction, a medium tries problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Build a trie of all suffixes (terminated by ' ') and answer contains(suffix).

## 3. Intuition (0:19) — `slides/03.png`

Insert every suffix into a trie, then any substring is a path from the root.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Storing suffixes in a list makes each lookup scan everything. A suffix trie builds in quadratic time and space and answers lookups in the length of the query.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, for each start index, insert the suffix. Second, mark ends with a star. Third, contains walks the trie.

## 6. Worked example (0:46) — `slides/06.png`

Insert the suffix b a b c, followed by an end marker.

## 7. Worked example (0:51) — `slides/07.png`

Insert the suffix a b c, followed by an end marker.

## 8. Worked example (0:55) — `slides/08.png`

Insert the suffix b c, followed by an end marker.

## 9. Worked example (1:00) — `slides/09.png`

Insert the suffix c, followed by an end marker.

## 10. Worked example (1:04) — `slides/10.png`

Contains walks the characters; it's true only if the final node has the end marker, so ab is not a suffix but abc is.

## 11. Java solution (1:12) — `slides/11.png`

The constructor inserts every suffix character by character, creating nodes as needed, then adds the end marker. Contains walks the characters and checks the end marker.

## 12. Complexity (1:22) — `slides/12.png`

Time is build O of n squared, contains O of m. Space is O of n squared.

## 13. Edge cases & pitfalls (1:28) — `slides/13.png`

The end marker distinguishes a true suffix from just a substring.

## 14. Interview tips & follow-ups (1:33) — `slides/14.png`

Mention suffix trees and arrays for linear-space alternatives.

## 15. Recap (1:38) — `slides/15.png`

To recap Suffix Trie Construction: Insert every suffix into a trie, then any substring is a path from the root. Try re-implementing it from scratch without looking.
