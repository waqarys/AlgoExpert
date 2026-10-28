# AlgoExpert · Min Max Stack Construction

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Max Stack Construction (0:00) — `slides/01.png`

Let's solve Min Max Stack Construction, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. A stack with constant push, pop, peek, getMin and getMax by storing the running min or max alongside each element.

## 3. Intuition (0:21) — `slides/03.png`

Store the current min and max alongside each pushed value so they're always available.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Scanning for min and max is linear per query. Storing the running min and max with each entry makes every operation constant time; popping automatically restores the old values.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, push value with updated min and max. Second, pop removes both. Third, peek, getMin and getMax read the top.

## 6. Worked example (0:50) — `slides/06.png`

Push 5. Each entry stores the min and max of everything at or below it, so the top answers min 5 and max 5 instantly.

## 7. Worked example (0:59) — `slides/07.png`

Push 7. Each entry stores the min and max of everything at or below it, so the top answers min 5 and max 7 instantly.

## 8. Worked example (1:08) — `slides/08.png`

Push 2. Each entry stores the min and max of everything at or below it, so the top answers min 2 and max 7 instantly.

## 9. Worked example (1:16) — `slides/09.png`

Pop. Each entry stores the min and max of everything at or below it, so the top answers min 5 and max 7 instantly.

## 10. Worked example (1:25) — `slides/10.png`

Push 9. Each entry stores the min and max of everything at or below it, so the top answers min 5 and max 9 instantly.

## 11. Java solution (1:34) — `slides/11.png`

Each push stores the value with the min and max of itself and the previous top. Peek and pop read the value; get min and get max read the top's stored fields.

## 12. Complexity (1:44) — `slides/12.png`

Time is constant per op. Space is O of n.

## 13. Edge cases & pitfalls (1:48) — `slides/13.png`

Popping needs no special handling, because the entry below already stores the correct min and max.

## 14. Interview tips & follow-ups (1:54) — `slides/14.png`

A follow-up uses an encoding trick to avoid storing extra values.

## 15. Recap (1:59) — `slides/15.png`

To recap Min Max Stack Construction: Store the current min and max alongside each pushed value so they're always available. Try re-implementing it from scratch without looking.
