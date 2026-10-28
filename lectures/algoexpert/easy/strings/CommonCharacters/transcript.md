# AlgoExpert · Common Characters

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Common Characters (0:00) — `slides/01.png`

Let's solve Common Characters, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return the unique characters that appear in every string.

## 3. Intuition (0:17) — `slides/03.png`

A character is common if it appears in every string, so count in how many strings each unique character appears.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Brute force would check each character of the first word against every other word. Counting how many words contain each distinct character does it in one pass over all the characters.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, for each string, take its set of characters. Second, count the number of strings containing each one. Third, keep characters whose count equals the number of strings.

## 6. Worked example (0:48) — `slides/06.png`

Process abc: each distinct character's count goes up by one. Characters with count 3 appear in every word so far.

## 7. Worked example (0:57) — `slides/07.png`

Process bcd: each distinct character's count goes up by one. Characters with count 3 appear in every word so far.

## 8. Worked example (1:05) — `slides/08.png`

Process cbad: each distinct character's count goes up by one. Characters with count 3 appear in every word so far.

## 9. Worked example (1:14) — `slides/09.png`

Characters that reached the number of words, b and c, are common to all of them.

## 10. Java solution (1:19) — `slides/10.png`

We loop over the strings, build a set of each string's characters, and increment counts in a map. Finally, we collect characters whose count equals the number of strings.

## 11. Complexity (1:30) — `slides/11.png`

Time is O of n times m. Space is O of c distinct chars.

## 12. Edge cases & pitfalls (1:35) — `slides/12.png`

Use a set per word so repeated letters count once. A single word returns all its unique characters.

## 13. Interview tips & follow-ups (1:42) — `slides/13.png`

An optimisation starts from the shortest word. A follow-up includes multiplicity, keeping minimum counts per character.

## 14. Recap (1:51) — `slides/14.png`

To recap Common Characters: A character is common if it appears in every string, so count in how many strings each unique character appears. Try re-implementing it from scratch without looking.
