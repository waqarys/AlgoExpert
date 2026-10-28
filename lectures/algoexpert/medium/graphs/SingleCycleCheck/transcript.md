# AlgoExpert · Single Cycle Check

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Single Cycle Check (0:00) — `slides/01.png`

Let's solve Single Cycle Check, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Each element is a jump (wrapping). Do the jumps form one cycle visiting every index exactly once and returning to the start?

## 3. Intuition (0:22) — `slides/03.png`

Follow the jumps n times: we must visit every index exactly once and return to the start.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

A visited array works but uses extra space. Counting is enough: if we make n jumps, never land on index zero early, and end at zero, every index was visited exactly once.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, jump n times with wrap-around. Second, if we return to zero early, fail. Third, after n jumps we must be at zero.

## 6. Worked example (0:52) — `slides/06.png`

From index 0, jump 2 to index 2, wrapping around if needed.

## 7. Worked example (0:57) — `slides/07.png`

From index 2, jump 1 to index 3, wrapping around if needed.

## 8. Worked example (1:02) — `slides/08.png`

From index 3, jump -4 to index 5, wrapping around if needed.

## 9. Worked example (1:08) — `slides/09.png`

From index 1, jump 3 to index 4, wrapping around if needed.

## 10. Worked example (1:13) — `slides/10.png`

From index 4, jump -4 to index 0, wrapping around if needed.

## 11. Worked example (1:18) — `slides/11.png`

After exactly 6 jumps, we're back at index zero, and we never returned early. It's a single cycle.

## 12. Java solution (1:26) — `slides/12.png`

We loop n times. If we land back on zero after at least one jump but before n jumps, we return false. Each step moves the index by the value with floor mod. Finally we check we're at zero.

## 13. Complexity (1:40) — `slides/13.png`

Time is O of n. Space is constant.

## 14. Edge cases & pitfalls (1:44) — `slides/14.png`

Use floor mod so negative jumps wrap correctly, and remember that returning to zero too early means a smaller cycle.

## 15. Interview tips & follow-ups (1:51) — `slides/15.png`

Explain the counting argument carefully; that's what interviewers look for.

## 16. Recap (1:56) — `slides/16.png`

To recap Single Cycle Check: Follow the jumps n times: we must visit every index exactly once and return to the start. Try re-implementing it from scratch without looking.
