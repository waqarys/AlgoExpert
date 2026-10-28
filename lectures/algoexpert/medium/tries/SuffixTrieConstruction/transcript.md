# AlgoExpert · Suffix Trie Construction

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Suffix Trie Construction (0:00) — `slides/01.png`

Let's solve Suffix Trie Construction, a medium tries problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Build a trie of all suffixes (terminated by ' ') and answer contains(suffix).

## 3. Intuition (0:19) — `slides/03.png`

Insert every suffix into a trie, then any substring is a path from the root.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, for each start index, insert the suffix. Second, mark ends with a star. Third, contains walks the trie.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with suffix trie. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is build O of n squared, contains O of m. Space is O of n squared.

## 7. Recap (0:49) — `slides/07.png`

To recap Suffix Trie Construction: Insert every suffix into a trie, then any substring is a path from the root. Try re-implementing it from scratch without looking.
