# AlgoExpert · Largest Island

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Largest Island (0:00) — `slides/01.png`

Let's solve Largest Island, a hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Matrix of 0 (land) and 1 (water). Flip at most one water cell to land to maximise the largest 4-connected land island; return its size. Label islands with ids and sizes first.

## 3. Intuition (0:26) — `slides/03.png`

Label each island with its size, then for each water cell sum the distinct neighbouring islands plus one.

## 4. Approach (0:33) — `slides/04.png`

Step by step. First, flood-fill to label islands and record sizes. Second, for each water cell, collect unique neighbouring labels. Third, sum sizes plus one. Fourth, take the max.

## 5. Java solution (1/2) (0:48) — `slides/05.png`

Here's the Java solution, starting with largest island. It follows the steps we just described.

## 6. Java solution (2/2) (0:55) — `slides/06.png`

Continuing the implementation.

## 7. Complexity (0:58) — `slides/07.png`

Time is O of w times h. Space is O of w times h.

## 8. Recap (1:03) — `slides/08.png`

To recap Largest Island: Label each island with its size, then for each water cell sum the distinct neighbouring islands plus one. Try re-implementing it from scratch without looking.
