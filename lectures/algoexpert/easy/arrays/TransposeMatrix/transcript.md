# AlgoExpert · Transpose Matrix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Transpose Matrix (0:00) — `slides/01.png`

Let's solve Transpose Matrix, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Flip a 2D matrix over its main diagonal.

## 3. Intuition (0:17) — `slides/03.png`

Transposing swaps rows and columns, so the cell at row i, column j moves to row j, column i.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

There's no faster approach than touching every cell once, so the question is really about getting indices right. Because the shape changes from R by C to C by R, we need a new matrix; an in-place swap only works when the matrix is square.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, allocate a matrix with the dimensions swapped. Second, copy each cell to its mirrored position. Third, return the new matrix.

## 6. Worked example (0:50) — `slides/06.png`

The value 1 at row 0, column 0 moves to row 0, column 0 of the result.

## 7. Worked example (0:56) — `slides/07.png`

The value 3 at row 0, column 2 moves to row 2, column 0 of the result.

## 8. Worked example (1:02) — `slides/08.png`

The value 5 at row 1, column 1 moves to row 1, column 1 of the result.

## 9. Worked example (1:08) — `slides/09.png`

The value 6 at row 1, column 2 moves to row 2, column 1 of the result.

## 10. Java solution (1:13) — `slides/10.png`

We allocate a matrix with columns and rows swapped, then two nested loops copy matrix i j into result j i.

## 11. Complexity (1:20) — `slides/11.png`

Time is O of w times h. Space is O of w times h.

## 12. Edge cases & pitfalls (1:25) — `slides/12.png`

The classic bug is allocating the result with the original dimensions. Test a single row and a single column input to catch it.

## 13. Interview tips & follow-ups (1:34) — `slides/13.png`

Good follow-ups are an in-place transpose for square matrices, swapping only cells above the diagonal, and rotating an image by ninety degrees, which is a transpose plus reversing each row.

## 14. Recap (1:45) — `slides/14.png`

To recap Transpose Matrix: Transposing swaps rows and columns, so the cell at row i, column j moves to row j, column i. Try re-implementing it from scratch without looking.
