# AlgoExpert · Find Three Largest Numbers

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Three Largest Numbers (0:00) — `slides/01.png`

Let's solve Find Three Largest Numbers, an easy searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return the three largest values (sorted ascending) without sorting the input.

## 3. Intuition (0:19) — `slides/03.png`

Keep a tiny sorted window of the three largest seen so far, and shift values into place as larger ones arrive.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, start with three empty slots. Second, compare each number with the largest slot first. Third, shift smaller values down to make room. Fourth, return the three values ascending.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with find three largest numbers. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:53) — `slides/07.png`

To recap Find Three Largest Numbers: Keep a tiny sorted window of the three largest seen so far, and shift values into place as larger ones arrive. Try re-implementing it from scratch without looking.
