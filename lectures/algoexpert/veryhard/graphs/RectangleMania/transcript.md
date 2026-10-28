# AlgoExpert · Rectangle Mania

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Rectangle Mania (0:00) — `slides/01.png`

Let's solve Rectangle Mania, a very hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Count axis-aligned rectangles whose four corners are all in the point set. Each pair forming a strictly up-right diagonal identifies one rectangle exactly once.

## 3. Intuition (0:23) — `slides/03.png`

Two points forming an up-right diagonal define a rectangle if the other two corners exist.

## 4. Approach (0:29) — `slides/04.png`

Step by step. First, put points in a set. Second, for each pair up and to the right. Third, check the other two corners. Fourth, count.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with rectangle mania. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n squared. Space is O of n.

## 7. Recap (0:55) — `slides/07.png`

To recap Rectangle Mania: Two points forming an up-right diagonal define a rectangle if the other two corners exist. Try re-implementing it from scratch without looking.
