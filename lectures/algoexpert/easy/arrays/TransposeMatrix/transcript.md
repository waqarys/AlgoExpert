# AlgoExpert · Transpose Matrix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Transpose Matrix (0:00) — `slides/01.png`

Let's solve Transpose Matrix, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Flip a 2D matrix over its main diagonal.

## 3. Intuition (0:17) — `slides/03.png`

Transposing swaps rows and columns, so the cell at row i, column j moves to row j, column i.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, allocate a matrix with the dimensions swapped. Second, copy each cell to its mirrored position. Third, return the new matrix.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with transpose matrix. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is O of w times h. Space is O of w times h.

## 7. Recap (0:48) — `slides/07.png`

To recap Transpose Matrix: Transposing swaps rows and columns, so the cell at row i, column j moves to row j, column i. Try re-implementing it from scratch without looking.
