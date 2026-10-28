# AlgoExpert · Four Number Sum

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Four Number Sum (0:00) — `slides/01.png`

Let's solve Four Number Sum, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. All quadruplets of distinct integers summing to target (any order). Store pair sums seen before index i, combine with pairs after i, so each quadruplet is reported once.

## 3. Intuition (0:24) — `slides/03.png`

Split the quadruplet into two pairs, and use a hash map of pair sums seen strictly before index i to avoid duplicates.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, for each i, look at pairs i with j after it and check target minus their sum in the map. Second, then add pairs k with i, k before i, to the map. Third, this ordering prevents reusing indices.

## 5. Java solution (0:47) — `slides/05.png`

Here's the Java solution, starting with four number sum. It follows the steps we just described.

## 6. Complexity (0:54) — `slides/06.png`

Time is O of n squared avg. Space is O of n squared.

## 7. Recap (0:59) — `slides/07.png`

To recap Four Number Sum: Split the quadruplet into two pairs, and use a hash map of pair sums seen strictly before index i to avoid duplicates. Try re-implementing it from scratch without looking.
