# AlgoExpert · Sunset Views

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sunset Views (0:00) — `slides/01.png`

Let's solve Sunset Views, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Buildings face EAST or WEST; return ascending indices of buildings that can see the sunset (strictly taller than everything in front of them in that direction).

## 3. Intuition (0:22) — `slides/03.png`

A building sees the sunset if it's taller than everything between it and the sun.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Checking every building against all the ones in front is quadratic. Scanning from the sunset side and tracking the tallest seen so far is linear.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, scan from the sunset side. Second, keep the running max. Third, buildings taller than the max can see. Fourth, return indices in order.

## 6. Worked example (0:49) — `slides/06.png`

Scanning from the east, building 7 has height 2. It's taller than everything east of it, so it sees the sunset.

## 7. Worked example (0:57) — `slides/07.png`

Scanning from the east, building 6 has height 3. It's taller than everything east of it, so it sees the sunset.

## 8. Worked example (1:06) — `slides/08.png`

Scanning from the east, building 4 has height 3. Something east of it is at least 3 tall, so it's blocked.

## 9. Worked example (1:14) — `slides/09.png`

Scanning from the east, building 3 has height 4. It's taller than everything east of it, so it sees the sunset.

## 10. Worked example (1:22) — `slides/10.png`

Scanning from the east, building 1 has height 5. It's taller than everything east of it, so it sees the sunset.

## 11. Worked example (1:30) — `slides/11.png`

Scanning from the east, building 0 has height 3. Something east of it is at least 5 tall, so it's blocked.

## 12. Java solution (1:38) — `slides/12.png`

We scan from the sunset side, adding an index whenever its height beats the running max, then reverse the list when facing east.

## 13. Complexity (1:46) — `slides/13.png`

Time is O of n. Space is O of n.

## 14. Edge cases & pitfalls (1:50) — `slides/14.png`

Equal height blocks the view. Return the indices in ascending order, so reverse when scanning east.

## 15. Interview tips & follow-ups (1:57) — `slides/15.png`

Mention the stack-based alternative scanning in the opposite direction.

## 16. Recap (2:02) — `slides/16.png`

To recap Sunset Views: A building sees the sunset if it's taller than everything between it and the sun. Try re-implementing it from scratch without looking.
