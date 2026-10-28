# AlgoExpert · Sweet And Savory

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sweet And Savory (0:00) — `slides/01.png`

Let's solve Sweet And Savory, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Dishes have negative (sweet) or positive (savory) flavour. Pick one sweet plus one savory whose sum is closest to target without exceeding it; return sweet, savory or 0, 0 .

## 3. Intuition (0:25) — `slides/03.png`

Sort sweet and savory dishes, then use two pointers to approach the target from below.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, split by sign and sort. Second, pointer on the mildest sweet and the smallest savory. Third, if the sum fits, record it and try a bigger savory. Fourth, otherwise try a sweeter dish.

## 5. Java solution (0:47) — `slides/05.png`

Here's the Java solution, starting with sweet and savory. It follows the steps we just described.

## 6. Complexity (0:55) — `slides/06.png`

Time is O of n log n. Space is O of n.

## 7. Recap (0:59) — `slides/07.png`

To recap Sweet And Savory: Sort sweet and savory dishes, then use two pointers to approach the target from below. Try re-implementing it from scratch without looking.
