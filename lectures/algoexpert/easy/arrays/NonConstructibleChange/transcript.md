# AlgoExpert · Non Constructible Change

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Non Constructible Change (0:00) — `slides/01.png`

Let's solve Non Constructible Change, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Given positive coin values, find the minimum amount that cannot be formed. Sort; if the next coin exceeds (reachable plus 1), reachable plus 1 is the answer.

## 3. Intuition (0:24) — `slides/03.png`

Sort the coins. If you can already build every amount up to some total, a coin bigger than total plus one leaves a gap you can never fill.

## 4. Approach (0:33) — `slides/04.png`

Step by step. First, sort the coins ascending. Second, track change, the largest amount you can build so far. Third, if a coin exceeds change plus one, return change plus one. Fourth, otherwise add the coin to change.

## 5. Java solution (0:50) — `slides/05.png`

Here's the Java solution, starting with non constructible change. It follows the steps we just described.

## 6. Complexity (0:58) — `slides/06.png`

Time is O of n log n. Space is constant (in-place sort).

## 7. Recap (1:02) — `slides/07.png`

To recap Non Constructible Change: Sort the coins. If you can already build every amount up to some total, a coin bigger than total plus one leaves a gap you can never fill. Try re-implementing it from scratch without looking.
