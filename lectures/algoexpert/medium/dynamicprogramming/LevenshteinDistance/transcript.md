# AlgoExpert · Levenshtein Distance

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Levenshtein Distance (0:00) — `slides/01.png`

Let's solve Levenshtein Distance, a medium dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Minimum single-char inserts or deletes or substitutions turning a into b.

## 3. Intuition (0:19) — `slides/03.png`

Dynamic programming over prefixes: each cell is the cheapest edit between two prefixes.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, row zero and column zero are insert or delete costs. Second, equal characters copy the diagonal. Third, otherwise one plus the min of insert, delete, replace. Fourth, two rows suffice.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with levenshtein distance. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n times m. Space is O of min(n, m).

## 7. Recap (0:55) — `slides/07.png`

To recap Levenshtein Distance: Dynamic programming over prefixes: each cell is the cheapest edit between two prefixes. Try re-implementing it from scratch without looking.
