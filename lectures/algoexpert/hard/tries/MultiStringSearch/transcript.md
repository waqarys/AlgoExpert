# AlgoExpert · Multi String Search

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Multi String Search (0:00) — `slides/01.png`

Let's solve Multi String Search, a hard tries problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. For each small string, does it occur in the big string? Trie of small strings, scanned from every start position of the big string.

## 3. Intuition (0:21) — `slides/03.png`

Put the small strings in a trie, then walk it from each position of the big string.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Searching for each small string separately repeats scans. A trie of the small strings lets each start index check all of them at once. Aho-Corasick makes it linear.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, build a trie. Second, start a walk at each index of the big string. Third, mark words found. Fourth, return booleans.

## 6. Worked example (0:51) — `slides/06.png`

Put all the small strings in a trie.

## 7. Worked example (0:55) — `slides/07.png`

From each index of the big string, walk the trie as far as letters match, recording any word endings.

## 8. Worked example (1:01) — `slides/08.png`

This, is, a and string are found; yo, bigger and kappa aren't.

## 9. Java solution (1:06) — `slides/09.png`

We build a trie with words at terminal nodes. For each start index, follow children while they exist, adding words. Then map each small to whether it was found.

## 10. Complexity (1:17) — `slides/10.png`

Time is O of ns plus bs where b is the big length, s the longest small. Space is O of ns.

## 11. Edge cases & pitfalls (1:25) — `slides/11.png`

Duplicates and overlaps are handled naturally by the set of found words.

## 12. Interview tips & follow-ups (1:30) — `slides/12.png`

Mention Aho-Corasick for true linear time.

## 13. Recap (1:34) — `slides/13.png`

To recap Multi String Search: Put the small strings in a trie, then walk it from each position of the big string. Try re-implementing it from scratch without looking.
