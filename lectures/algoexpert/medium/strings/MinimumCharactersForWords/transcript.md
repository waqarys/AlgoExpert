# AlgoExpert · Minimum Characters For Words

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Minimum Characters For Words (0:00) — `slides/01.png`

Let's solve Minimum Characters For Words, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Smallest multiset of characters that can spell each word (one at a time).

## 3. Intuition (0:19) — `slides/03.png`

For each character, we need the maximum count it reaches in any single word.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Counting all characters together overcounts. What matters is, for each character, the maximum number of times any single word uses it.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, count characters per word. Second, keep the max per character. Third, emit each character that many times.

## 6. Worked example (0:45) — `slides/06.png`

After this, each character's count is the max it needs in any single word.

## 7. Worked example (0:50) — `slides/07.png`

After that, each character's count is the max it needs in any single word.

## 8. Worked example (0:55) — `slides/08.png`

After deed, each character's count is the max it needs in any single word.

## 9. Worked example (1:00) — `slides/09.png`

After them!, each character's count is the max it needs in any single word.

## 10. Java solution (1:05) — `slides/10.png`

For each word we count its characters and merge into need with max. Then we expand need into a character array.

## 11. Complexity (1:13) — `slides/11.png`

Time is O of n times l. Space is O of c.

## 12. Edge cases & pitfalls (1:17) — `slides/12.png`

Take the max per character, not the sum. Punctuation counts too.

## 13. Interview tips & follow-ups (1:23) — `slides/13.png`

Explain why max is correct: one word at a time.

## 14. Recap (1:27) — `slides/14.png`

To recap Minimum Characters For Words: For each character, we need the maximum count it reaches in any single word. Try re-implementing it from scratch without looking.
