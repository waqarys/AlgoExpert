# AlgoExpert · Minimum Passes Of Matrix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Minimum Passes Of Matrix (0:00) — `slides/01.png`

Let's solve Minimum Passes Of Matrix, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Each pass, every negative adjacent to a positive flips sign. Return the number of passes to clear all negatives, or -1 if impossible. Multi-source BFS by levels.

## 3. Intuition (0:26) — `slides/03.png`

Multi-source BFS: each pass, positives flip their negative neighbours.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Simulating each pass by rescanning the whole matrix can be quadratic in the number of cells. Multi-source breadth-first search starts from all positives at once, and each BFS level is exactly one pass.

## 5. Approach (0:44) — `slides/05.png`

Step by step. First, queue all positives. Second, process one level per pass. Third, flip negative neighbours and enqueue them. Fourth, if negatives remain, return minus one.

## 6. Worked example (0:59) — `slides/06.png`

Every positive cell starts in the queue. Each pass, they flip their negative neighbours.

## 7. Worked example (1:06) — `slides/07.png`

Pass 1: 3 negative cells next to positives become positive. They join the queue for the next pass.

## 8. Worked example (1:13) — `slides/08.png`

Pass 2: 4 negative cells next to positives become positive. They join the queue for the next pass.

## 9. Worked example (1:21) — `slides/09.png`

Pass 3: 1 negative cells next to positives become positive. They join the queue for the next pass.

## 10. Worked example (1:29) — `slides/10.png`

No negatives remain, so the answer is 3 passes.

## 11. Java solution (1:33) — `slides/11.png`

We enqueue all positive cells. Each round processes the current queue size, flips negative neighbours and enqueues them, and counts the pass if anything flipped. At the end, any remaining negative means minus one.

## 12. Complexity (1:47) — `slides/12.png`

Time is O of w times h. Space is O of w times h.

## 13. Edge cases & pitfalls (1:52) — `slides/13.png`

If some negatives are surrounded by zeros, return minus one. With no negatives, the answer is zero, so only count passes that flip something.

## 14. Interview tips & follow-ups (2:02) — `slides/14.png`

This is the rotting oranges pattern. Explain that BFS levels correspond exactly to passes.

## 15. Recap (2:10) — `slides/15.png`

To recap Minimum Passes Of Matrix: Multi-source BFS: each pass, positives flip their negative neighbours. Try re-implementing it from scratch without looking.
