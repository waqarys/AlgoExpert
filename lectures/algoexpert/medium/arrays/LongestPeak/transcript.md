# AlgoExpert · Longest Peak

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Peak (0:00) — `slides/01.png`

Let's solve Longest Peak, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Length of the longest strictly-increasing-then-strictly-decreasing run (needs over equals 3 items).

## 3. Intuition (0:19) — `slides/03.png`

A peak is a strict rise then a strict fall, so find each tip and expand both ways.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Expanding from every index is quadratic. Instead, only tips, values higher than both neighbours, can be peaks. Expanding from each tip and then jumping to the peak's end means each element is touched a constant number of times.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, find indices higher than both neighbours. Second, expand left while values keep decreasing outward. Third, expand right likewise. Fourth, track the longest span.

## 6. Worked example (0:55) — `slides/06.png`

Index 4, value 4, is higher than both neighbours, so it's a tip. Expanding left while values fall and right while values fall gives a peak from 3 to 5, length 3.

## 7. Worked example (1:06) — `slides/07.png`

Index 6, value 10, is higher than both neighbours, so it's a tip. Expanding left while values fall and right while values fall gives a peak from 5 to 10, length 6.

## 8. Java solution (1:17) — `slides/08.png`

We scan from index one. When the current value is a tip, we walk l left while values keep increasing toward the tip and r right while they keep decreasing, update the best length, and jump i to r. Otherwise i moves on.

## 9. Complexity (1:30) — `slides/09.png`

Time is O of n. Space is constant.

## 10. Edge cases & pitfalls (1:34) — `slides/10.png`

Inequalities are strict, so a plateau breaks a peak. A purely increasing array has no peak and returns zero.

## 11. Interview tips & follow-ups (1:42) — `slides/11.png`

Sketching the values as a mountain range makes this easy to explain. Variants ask for the longest valley.

## 12. Recap (1:50) — `slides/12.png`

To recap Longest Peak: A peak is a strict rise then a strict fall, so find each tip and expand both ways. Try re-implementing it from scratch without looking.
