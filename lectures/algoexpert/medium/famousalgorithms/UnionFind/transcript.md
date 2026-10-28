# AlgoExpert · Union Find

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Union Find (0:00) — `slides/01.png`

Let's solve Union Find, a medium famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Disjoint-set with createSet, find (null if unknown) and union, using path compression and union by rank.

## 3. Intuition (0:20) — `slides/03.png`

Each set is a tree with a representative root; path compression and union by rank keep trees flat.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Storing a set ID per element makes union linear, since you relabel a whole set. Parent pointers make union cheap, but trees can become long chains. Union by rank plus path compression keeps operations effectively constant, inverse-Ackermann time.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, createSet makes a single-node tree. Second, find follows parents with path compression. Third, union attaches the shorter tree under the taller.

## 6. Worked example (0:56) — `slides/06.png`

Create five sets. Every node is its own parent, so each is a root.

## 7. Worked example (1:03) — `slides/07.png`

Union 0 and 1: their roots are 0 and 1. Equal ranks, so the second root goes under the first and its rank grows.

## 8. Worked example (1:11) — `slides/08.png`

Union 2 and 3: their roots are 2 and 3. Equal ranks, so the second root goes under the first and its rank grows.

## 9. Worked example (1:20) — `slides/09.png`

Union 0 and 3: their roots are 0 and 2. Equal ranks, so the second root goes under the first and its rank grows.

## 10. Worked example (1:29) — `slides/10.png`

Finding three walks up to the root, zero, and compresses the path so three points straight at zero next time.

## 11. Java solution (1:36) — `slides/11.png`

Create set makes a node its own parent with rank zero. Find recursively finds the root and rewrites the parent pointer to it, which is path compression. Union finds both roots and attaches the lower-rank root under the higher one, bumping rank on ties.

## 12. Complexity (1:51) — `slides/12.png`

Time is about O of alpha(n) amortised per op. Space is O of n.

## 13. Edge cases & pitfalls (1:57) — `slides/13.png`

Return null for unknown values, and make union a no-op when both are already in the same set.

## 14. Interview tips & follow-ups (2:03) — `slides/14.png`

Union-find powers Kruskal's algorithm and dynamic connectivity. Union by size works as well as rank.

## 15. Recap (2:11) — `slides/15.png`

To recap Union Find: Each set is a tree with a representative root; path compression and union by rank keep trees flat. Try re-implementing it from scratch without looking.
