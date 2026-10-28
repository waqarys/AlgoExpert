# AlgoExpert · Tandem Bicycle

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Tandem Bicycle (0:00) — `slides/01.png`

Let's solve Tandem Bicycle, an easy greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Pair red and blue riders; a tandem's speed is the max of its riders. Return the max (fastest equals true) or min possible total speed.

## 3. Intuition (0:23) — `slides/03.png`

Speed is the max of the two riders. For maximum total, pair the fastest with the slowest; for minimum, pair like with like.

## 4. Approach (0:32) — `slides/04.png`

Step by step. First, sort both lists. Second, for fastest total, pair one ascending with the other descending. Third, for slowest, pair in the same order. Fourth, sum the max of each pair.

## 5. Java solution (0:47) — `slides/05.png`

Here's the Java solution, starting with tandem bicycle. It follows the steps we just described.

## 6. Complexity (0:55) — `slides/06.png`

Time is O of n log n. Space is constant.

## 7. Recap (0:59) — `slides/07.png`

To recap Tandem Bicycle: Speed is the max of the two riders. For maximum total, pair the fastest with the slowest; for minimum, pair like with like. Try re-implementing it from scratch without looking.
