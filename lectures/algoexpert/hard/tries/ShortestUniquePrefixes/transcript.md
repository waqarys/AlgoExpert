# AlgoExpert · Shortest Unique Prefixes

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Shortest Unique Prefixes (0:00) — `slides/01.png`

Let's solve Shortest Unique Prefixes, a hard tries problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. For each unique string, the shortest prefix that no other string shares; if a string is a prefix of another, its answer is the whole string. Trie with per-node counts.

## 3. Intuition (0:23) — `slides/03.png`

A trie with counts tells us the first depth where only one string passes through.

## 4. Approach (0:29) — `slides/04.png`

Step by step. First, insert all strings counting. Second, for each string, walk until a count of one. Third, return that prefix, or the full string.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with shortest unique prefixes. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n times m. Space is O of n times m.

## 7. Recap (0:53) — `slides/07.png`

To recap Shortest Unique Prefixes: A trie with counts tells us the first depth where only one string passes through. Try re-implementing it from scratch without looking.
