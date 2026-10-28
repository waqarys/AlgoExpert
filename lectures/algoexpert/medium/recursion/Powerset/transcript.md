# AlgoExpert · Powerset

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Powerset (0:00) — `slides/01.png`

Let's solve Powerset, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Every subset of a set of distinct ints (iteratively doubling).

## 3. Intuition (0:18) — `slides/03.png`

Each new element doubles the subsets: every existing subset with or without it.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, start with the empty set. Second, for each element, copy all subsets and add it. Third, return all.

## 5. Java solution (0:35) — `slides/05.png`

Here's the Java solution, starting with powerset. It follows the steps we just described.

## 6. Complexity (0:42) — `slides/06.png`

Time is O of n times 2 to the n. Space is O of n times 2 to the n.

## 7. Recap (0:47) — `slides/07.png`

To recap Powerset: Each new element doubles the subsets: every existing subset with or without it. Try re-implementing it from scratch without looking.
