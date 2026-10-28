# AlgoExpert · Minimum Characters For Words

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Minimum Characters For Words (0:00) — `slides/01.png`

Let's solve Minimum Characters For Words, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Smallest multiset of characters that can spell each word (one at a time).

## 3. Intuition (0:19) — `slides/03.png`

For each character, we need the maximum count it reaches in any single word.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, count characters per word. Second, keep the max per character. Third, emit each character that many times.

## 5. Java solution (0:35) — `slides/05.png`

Here's the Java solution, starting with minimum characters for words. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is O of n times l. Space is O of c.

## 7. Recap (0:47) — `slides/07.png`

To recap Minimum Characters For Words: For each character, we need the maximum count it reaches in any single word. Try re-implementing it from scratch without looking.
