# AlgoExpert · Largest Park

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Largest Park (0:00) — `slides/01.png`

Let's solve Largest Park, a very hard stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Boolean matrix where false is free land and true is in use. Area of the largest all-free rectangle (0 if none). For each row build a histogram of consecutive free cells above and take the largest rectangle in it with a monotonic stack.

## 3. Intuition (0:28) — `slides/03.png`

Treat each row as a histogram of free heights and apply the largest rectangle in histogram.

## 4. Approach (0:34) — `slides/04.png`

Step by step. First, update column heights per row. Second, run the monotonic stack. Third, track the max area.

## 5. Java solution (1/2) (0:45) — `slides/05.png`

Here's the Java solution, starting with largest park. It follows the steps we just described.

## 6. Java solution (2/2) (0:52) — `slides/06.png`

Continuing with largest rectangle.

## 7. Complexity (0:55) — `slides/07.png`

Time is O of w times h. Space is O of w.

## 8. Recap (1:00) — `slides/08.png`

To recap Largest Park: Treat each row as a histogram of free heights and apply the largest rectangle in histogram. Try re-implementing it from scratch without looking.
