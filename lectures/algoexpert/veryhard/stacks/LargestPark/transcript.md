# AlgoExpert · Largest Park

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Largest Park (0:00) — `slides/01.png`

Let's solve Largest Park, a very hard stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Boolean matrix where false is free land and true is in use. Area of the largest all-free rectangle (0 if none). For each row build a histogram of consecutive free cells above and take the largest rectangle in it with a monotonic stack.

## 3. Intuition (0:28) — `slides/03.png`

Treat each row as a histogram of free heights and apply the largest rectangle in histogram.

## 4. Brute force vs optimal (0:34) — `slides/04.png`

Checking every rectangle is huge. Treating each row as the base of a histogram and using the skyline stack is linear in the grid.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, update column heights per row. Second, run the monotonic stack. Third, track the max area.

## 6. Worked example (0:54) — `slides/06.png`

After row 0, each column's height counts free cells above. The best rectangle in this histogram is 2.

## 7. Worked example (1:02) — `slides/07.png`

After row 1, each column's height counts free cells above. The best rectangle in this histogram is 4.

## 8. Worked example (1:09) — `slides/08.png`

After row 2, each column's height counts free cells above. The best rectangle in this histogram is 4.

## 9. Worked example (1:17) — `slides/09.png`

After row 3, each column's height counts free cells above. The best rectangle in this histogram is 6.

## 10. Java solution (1/2) (1:25) — `slides/10.png`

For each row, update heights, then compute the largest rectangle under that histogram with the stack method, tracking the best.

## 11. Java solution (2/2) (1:33) — `slides/11.png`

For each row, update heights, then compute the largest rectangle under that histogram with the stack method, tracking the best.

## 12. Complexity (1:41) — `slides/12.png`

Time is O of w times h. Space is O of w.

## 13. Edge cases & pitfalls (1:45) — `slides/13.png`

A blocked cell resets that column's height to zero.

## 14. Interview tips & follow-ups (1:49) — `slides/14.png`

This is maximal rectangle.

## 15. Recap (1:52) — `slides/15.png`

To recap Largest Park: Treat each row as a histogram of free heights and apply the largest rectangle in histogram. Try re-implementing it from scratch without looking.
