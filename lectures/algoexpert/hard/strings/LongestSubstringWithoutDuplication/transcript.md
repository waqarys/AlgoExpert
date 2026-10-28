# AlgoExpert · Longest Substring Without Duplication

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Substring Without Duplication (0:00) — `slides/01.png`

Let's solve Longest Substring Without Duplication, a hard strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Sliding window with last-seen index per character.

## 3. Intuition (0:18) — `slides/03.png`

Slide a window; when a character repeats, jump the start past its last occurrence.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Checking every substring for duplicates is cubic. A sliding window with a last-seen map lets the start jump past a repeat directly, linear time.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, map characters to last index. Second, move start past a repeat. Third, track the longest window.

## 6. Worked example (0:44) — `slides/06.png`

At c, no repeat. The best is c.

## 7. Worked example (0:49) — `slides/07.png`

At e, it already appeared in the window, so the start jumps past it to index 3. The best is clem.

## 8. Worked example (0:57) — `slides/08.png`

At t, no repeat. The best is clem.

## 9. Worked example (1:02) — `slides/09.png`

At a, it already appeared in the window, so the start jumps past it to index 10. The best is mentisac.

## 10. Worked example (1:10) — `slides/10.png`

At p, no repeat. The best is mentisac.

## 11. Java solution (1:15) — `slides/11.png`

For each index, if the character's last position is within the window, move start past it. Update last and the best.

## 12. Complexity (1:23) — `slides/12.png`

Time is O of n. Space is O of min(n, a).

## 13. Edge cases & pitfalls (1:28) — `slides/13.png`

Only move the start if the previous occurrence is inside the window.

## 14. Interview tips & follow-ups (1:32) — `slides/14.png`

A fixed-size array works as the map for ASCII.

## 15. Recap (1:37) — `slides/15.png`

To recap Longest Substring Without Duplication: Slide a window; when a character repeats, jump the start past its last occurrence. Try re-implementing it from scratch without looking.
