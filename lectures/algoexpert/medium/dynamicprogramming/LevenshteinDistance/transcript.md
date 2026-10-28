# AlgoExpert · Levenshtein Distance

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Levenshtein Distance (0:00) — `slides/01.png`

Let's solve Levenshtein Distance, a medium dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Minimum single-char inserts or deletes or substitutions turning a into b.

## 3. Intuition (0:19) — `slides/03.png`

Dynamic programming over prefixes: each cell is the cheapest edit between two prefixes.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Recursively trying every edit branches three ways at each step, which is exponential. The same subproblems repeat, so a table over prefixes solves it in n times m. Since each row only needs the previous one, two rows suffice.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, row zero and column zero are insert or delete costs. Second, equal characters copy the diagonal. Third, otherwise one plus the min of insert, delete, replace. Fourth, two rows suffice.

## 6. Worked example (0:58) — `slides/06.png`

The first row and column are the cost of building a prefix from nothing: just insertions or deletions.

## 7. Worked example (1:04) — `slides/07.png`

Turning a into ya: the last letters are both a, so the cost equals the diagonal, 1.

## 8. Worked example (1:10) — `slides/08.png`

Turning ab into yab: the last letters are both b, so the cost equals the diagonal, 1.

## 9. Worked example (1:16) — `slides/09.png`

Turning abc into yab: the last letters differ, so we pay one plus the cheapest of replace, delete or insert: 2.

## 10. Worked example (1:24) — `slides/10.png`

Turning abc into yabd: the last letters differ, so we pay one plus the cheapest of replace, delete or insert: 2.

## 11. Java solution (1:32) — `slides/11.png`

We swap so b is the shorter string, initialise the previous row to zero through m, and for each character of a fill the current row: equal characters copy the diagonal, otherwise one plus the min of the three neighbours. Then we swap rows and return the last value.

## 12. Complexity (1:47) — `slides/12.png`

Time is O of n times m. Space is O of min(n, m).

## 13. Edge cases & pitfalls (1:52) — `slides/13.png`

If either string is empty, the answer is the other's length. The table has one extra row and column for the empty prefix, a common off-by-one trap.

## 14. Interview tips & follow-ups (2:01) — `slides/14.png`

Name the three neighbours explicitly: diagonal is replace, above is delete, left is insert. Follow-ups reconstruct the edit script or use weighted costs.

## 15. Recap (2:12) — `slides/15.png`

To recap Levenshtein Distance: Dynamic programming over prefixes: each cell is the cheapest edit between two prefixes. Try re-implementing it from scratch without looking.
