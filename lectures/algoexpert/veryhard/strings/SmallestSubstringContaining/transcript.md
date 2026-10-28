# AlgoExpert · Smallest Substring Containing

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Smallest Substring Containing (0:00) — `slides/01.png`

Let's solve Smallest Substring Containing, a very hard strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Shortest substring of big containing every character of small (with multiplicity), or "". Sliding window.

## 3. Intuition (0:22) — `slides/03.png`

A sliding window expands until it covers all needed characters, then shrinks to the minimum.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Checking every substring is quadratic or worse. A sliding window with a count of missing characters is linear.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, count needed characters. Second, expand right updating coverage. Third, shrink left while still covering. Fourth, track the smallest window.

## 6. Worked example (0:50) — `slides/06.png`

Find the smallest substring of big containing every character of small, with multiplicity.

## 7. Worked example (0:56) — `slides/07.png`

Expand the right end until nothing is missing, then shrink from the left while it stays valid, recording the best.

## 8. Worked example (1:03) — `slides/08.png`

The smallest such window is f, dollar, a, x, b, dollar.

## 9. Java solution (1:08) — `slides/09.png`

We count needs, decrement missing as r covers needed characters, and while missing is zero record the window and advance l, restoring needs.

## 10. Complexity (1:17) — `slides/10.png`

Time is O of b plus s. Space is O of s.

## 11. Edge cases & pitfalls (1:21) — `slides/11.png`

Duplicates in small must be matched in count.

## 12. Interview tips & follow-ups (1:24) — `slides/12.png`

This is minimum window substring.

## 13. Recap (1:28) — `slides/13.png`

To recap Smallest Substring Containing: A sliding window expands until it covers all needed characters, then shrinks to the minimum. Try re-implementing it from scratch without looking.
