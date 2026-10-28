# AlgoExpert · Index Equals Value

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Index Equals Value (0:00) — `slides/01.png`

Let's solve Index Equals Value, a hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sorted distinct ints; smallest index i with a i equals equals i, or -1. Binary search.

## 3. Intuition (0:21) — `slides/03.png`

Since values are distinct sorted integers, value minus index never decreases, so binary search works.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, binary search. Second, if the value is below the index, go right. Third, otherwise record a match and go left for the smallest.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with index equals value. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of log n. Space is constant.

## 7. Recap (0:52) — `slides/07.png`

To recap Index Equals Value: Since values are distinct sorted integers, value minus index never decreases, so binary search works. Try re-implementing it from scratch without looking.
