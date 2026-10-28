# AlgoExpert · Shortest Unique Prefixes

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Shortest Unique Prefixes (0:00) — `slides/01.png`

Let's solve Shortest Unique Prefixes, a hard tries problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. For each unique string, the shortest prefix that no other string shares; if a string is a prefix of another, its answer is the whole string. Trie with per-node counts.

## 3. Intuition (0:23) — `slides/03.png`

A trie with counts tells us the first depth where only one string passes through.

## 4. Brute force vs optimal (0:29) — `slides/04.png`

Comparing every pair of words is quadratic. A trie with counts finds each word's first unique node in its own length.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, insert all strings counting. Second, for each string, walk until a count of one. Third, return that prefix, or the full string.

## 6. Worked example (0:49) — `slides/06.png`

Insert each word, counting how many words pass through each node.

## 7. Worked example (0:54) — `slides/07.png`

For each word, the shortest unique prefix ends at the first node with count one.

## 8. Java solution (0:59) — `slides/08.png`

We insert all words with counts, then for each word walk until a node's count is one, returning the prefix up to there or the whole word.

## 9. Complexity (1:07) — `slides/09.png`

Time is O of n times m. Space is O of n times m.

## 10. Edge cases & pitfalls (1:12) — `slides/10.png`

If a word is a prefix of another, the answer is the whole word.

## 11. Interview tips & follow-ups (1:16) — `slides/11.png`

Explain that the count is how many words share the prefix.

## 12. Recap (1:21) — `slides/12.png`

To recap Shortest Unique Prefixes: A trie with counts tells us the first depth where only one string passes through. Try re-implementing it from scratch without looking.
