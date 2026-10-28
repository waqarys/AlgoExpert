# AlgoExpert · Minimum Passes Of Matrix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Minimum Passes Of Matrix (0:00) — `slides/01.png`

Let's solve Minimum Passes Of Matrix, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Each pass, every negative adjacent to a positive flips sign. Return the number of passes to clear all negatives, or -1 if impossible. Multi-source BFS by levels.

## 3. Intuition (0:26) — `slides/03.png`

Multi-source BFS: each pass, positives flip their negative neighbours.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, queue all positives. Second, process one level per pass. Third, flip negative neighbours and enqueue them. Fourth, if negatives remain, return minus one.

## 5. Java solution (0:46) — `slides/05.png`

Here's the Java solution, starting with minimum passes of matrix. It follows the steps we just described.

## 6. Complexity (0:54) — `slides/06.png`

Time is O of w times h. Space is O of w times h.

## 7. Recap (0:59) — `slides/07.png`

To recap Minimum Passes Of Matrix: Multi-source BFS: each pass, positives flip their negative neighbours. Try re-implementing it from scratch without looking.
