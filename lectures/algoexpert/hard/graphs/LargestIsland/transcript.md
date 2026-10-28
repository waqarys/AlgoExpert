# AlgoExpert · Largest Island

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Largest Island (0:00) — `slides/01.png`

Let's solve Largest Island, a hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Matrix of 0 (land) and 1 (water). Flip at most one water cell to land to maximise the largest 4-connected land island; return its size. Label islands with ids and sizes first.

## 3. Intuition (0:26) — `slides/03.png`

Label each island with its size, then for each water cell sum the distinct neighbouring islands plus one.

## 4. Brute force vs optimal (0:33) — `slides/04.png`

Flipping each water cell and flood-filling again is quadratic in the grid size. Label islands once with their sizes, then each water cell just sums its distinct neighbouring islands.

## 5. Approach (0:44) — `slides/05.png`

Step by step. First, flood-fill to label islands and record sizes. Second, for each water cell, collect unique neighbouring labels. Third, sum sizes plus one. Fourth, take the max.

## 6. Worked example (0:59) — `slides/06.png`

Here zeros are land and ones are water. We may flip one water cell to land; what's the largest island?

## 7. Worked example (1:07) — `slides/07.png`

First label each island and record its size: A has three cells, B has one.

## 8. Worked example (1:12) — `slides/08.png`

Now for each water cell, add one plus the sizes of the distinct islands next to it. Flipping row one, column two joins A and B: five.

## 9. Java solution (1/2) (1:22) — `slides/09.png`

We label each land component with an ID from two upward and record its size. Then for each water cell we collect distinct neighbouring IDs, sum one plus their sizes, and keep the best.

## 10. Java solution (2/2) (1:33) — `slides/10.png`

We label each land component with an ID from two upward and record its size. Then for each water cell we collect distinct neighbouring IDs, sum one plus their sizes, and keep the best.

## 11. Complexity (1:45) — `slides/11.png`

Time is O of w times h. Space is O of w times h.

## 12. Edge cases & pitfalls (1:50) — `slides/12.png`

Use a set of island IDs so an island touching a cell from two sides isn't counted twice. If there's no water, the answer is the whole grid.

## 13. Interview tips & follow-ups (1:59) — `slides/13.png`

This is making a large island.

## 14. Recap (2:02) — `slides/14.png`

To recap Largest Island: Label each island with its size, then for each water cell sum the distinct neighbouring islands plus one. Try re-implementing it from scratch without looking.
