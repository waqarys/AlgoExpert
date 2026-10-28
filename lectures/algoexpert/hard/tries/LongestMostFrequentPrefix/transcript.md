# AlgoExpert · Longest Most Frequent Prefix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Most Frequent Prefix (0:00) — `slides/01.png`

Let's solve Longest Most Frequent Prefix, a hard tries problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Given unique strings, return the prefix shared by the most strings; ties go to the longest such prefix. Trie storing per-node counts.

## 3. Intuition (0:22) — `slides/03.png`

A trie with counts at each node gives every prefix's frequency directly.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Counting every prefix as a separate string costs quadratic memory. A trie with counts does it in total characters.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, insert strings counting passes per node. Second, track the max count and longest depth. Third, return that prefix.

## 6. Worked example (0:48) — `slides/06.png`

Insert every word into a trie, incrementing a count on each node passed.

## 7. Worked example (0:53) — `slides/07.png`

Prefixes a through algo each appear twice; others once.

## 8. Worked example (0:58) — `slides/08.png`

The highest count is 2, and the longest prefix with that count is algo.

## 9. Java solution (1:03) — `slides/09.png`

We insert each string, incrementing counts. Then we walk each string again, updating the best when a node's count is higher, or equal with a longer prefix.

## 10. Complexity (1:13) — `slides/10.png`

Time is O of n times m. Space is O of n times m.

## 11. Edge cases & pitfalls (1:17) — `slides/11.png`

On ties in count, prefer the longer prefix.

## 12. Interview tips & follow-ups (1:21) — `slides/12.png`

Explain that node counts are prefix frequencies.

## 13. Recap (1:25) — `slides/13.png`

To recap Longest Most Frequent Prefix: A trie with counts at each node gives every prefix's frequency directly. Try re-implementing it from scratch without looking.
