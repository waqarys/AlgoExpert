# AlgoExpert · Union Find

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Union Find (0:00) — `slides/01.png`

Let's solve Union Find, a medium famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Disjoint-set with createSet, find (null if unknown) and union, using path compression and union by rank.

## 3. Intuition (0:20) — `slides/03.png`

Each set is a tree with a representative root; path compression and union by rank keep trees flat.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, createSet makes a single-node tree. Second, find follows parents with path compression. Third, union attaches the shorter tree under the taller.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with create set. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is about O of alpha(n) amortised per op. Space is O of n.

## 7. Recap (0:52) — `slides/07.png`

To recap Union Find: Each set is a tree with a representative root; path compression and union by rank keep trees flat. Try re-implementing it from scratch without looking.
