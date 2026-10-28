# AlgoExpert · Common Characters

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Common Characters (0:00) — `slides/01.png`

Let's solve Common Characters, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return the unique characters that appear in every string.

## 3. Intuition (0:17) — `slides/03.png`

A character is common if it appears in every string, so count in how many strings each unique character appears.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, for each string, take its set of characters. Second, count the number of strings containing each one. Third, keep characters whose count equals the number of strings.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with common characters. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n times m. Space is O of c distinct chars.

## 7. Recap (0:50) — `slides/07.png`

To recap Common Characters: A character is common if it appears in every string, so count in how many strings each unique character appears. Try re-implementing it from scratch without looking.
