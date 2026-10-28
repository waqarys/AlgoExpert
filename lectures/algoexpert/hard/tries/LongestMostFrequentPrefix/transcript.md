# AlgoExpert · Longest Most Frequent Prefix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Most Frequent Prefix (0:00) — `slides/01.png`

Let's solve Longest Most Frequent Prefix, a hard tries problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Given unique strings, return the prefix shared by the most strings; ties go to the longest such prefix. Trie storing per-node counts.

## 3. Intuition (0:22) — `slides/03.png`

A trie with counts at each node gives every prefix's frequency directly.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, insert strings counting passes per node. Second, track the max count and longest depth. Third, return that prefix.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with longest most frequent prefix. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of n times m. Space is O of n times m.

## 7. Recap (0:52) — `slides/07.png`

To recap Longest Most Frequent Prefix: A trie with counts at each node gives every prefix's frequency directly. Try re-implementing it from scratch without looking.
