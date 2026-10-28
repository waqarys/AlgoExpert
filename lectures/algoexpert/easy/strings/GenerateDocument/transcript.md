# AlgoExpert · Generate Document

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Generate Document (0:00) — `slides/01.png`

Let's solve Generate Document, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Can document be built from the multiset of characters in characters?

## 3. Intuition (0:18) — `slides/03.png`

We can build the document if, for every character, we have at least as many copies available as needed.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Recounting each character in both strings is quadratic. Counting the available characters once and decrementing for the document is linear, and we can stop as soon as a count goes negative.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, count available characters. Second, for each document character, decrement its count. Third, if any count goes negative, return false.

## 6. Worked example (0:49) — `slides/06.png`

We count every available character, including spaces and punctuation.

## 7. Worked example (0:54) — `slides/07.png`

Use one A; 0 left.

## 8. Worked example (0:57) — `slides/08.png`

Use one E; 0 left.

## 9. Worked example (1:01) — `slides/09.png`

Use one h; 0 left.

## 10. Worked example (1:04) — `slides/10.png`

Every character of the document was available, so the answer is true.

## 11. Java solution (1:09) — `slides/11.png`

We count the available characters in a map, then for each document character decrement its count and return false if it drops below zero.

## 12. Complexity (1:17) — `slides/12.png`

Time is O of n plus m. Space is O of c.

## 13. Edge cases & pitfalls (1:21) — `slides/13.png`

Matching is case-sensitive and spaces count. An empty document can always be generated.

## 14. Interview tips & follow-ups (1:28) — `slides/14.png`

Ask about the character set. If you need to answer for many documents, reuse the counts.

## 15. Recap (1:35) — `slides/15.png`

To recap Generate Document: We can build the document if, for every character, we have at least as many copies available as needed. Try re-implementing it from scratch without looking.
