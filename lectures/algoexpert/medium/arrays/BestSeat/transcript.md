# AlgoExpert · Best Seat

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Best Seat (0:00) — `slides/01.png`

Let's solve Best Seat, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. A row of seats (1 taken, 0 free; both ends taken). Return the index of the free seat with the most space on both sides (centre of the widest gap, leftmost on ties), or -1.

## 3. Intuition (0:25) — `slides/03.png`

The best seat is the middle of the longest run of empty seats between occupied ones.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

Brute force checks each empty seat and scans outward for the nearest people, which is quadratic. Instead we walk once, measuring each run of empty seats between occupied ones, and keep the middle of the longest.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, scan for runs of zeros between ones. Second, track the longest run. Third, return its middle index, or minus one if none.

## 6. Worked example (0:55) — `slides/06.png`

Between occupied seats 0 and 2 there is 1 empty seat. The middle is seat 1.

## 7. Worked example (1:02) — `slides/07.png`

Between occupied seats 2 and 6 there are 3 empty seats. The middle is seat 4.

## 8. Java solution (1:09) — `slides/08.png`

We start at an occupied seat l, move r forward past zeros, compute the gap as r minus l minus one, and if it's the best so far, record the middle seat. Then l jumps to r.

## 9. Complexity (1:20) — `slides/09.png`

Time is O of n. Space is constant.

## 10. Edge cases & pitfalls (1:24) — `slides/10.png`

If there's no empty seat, return minus one. Using a strictly greater comparison keeps the leftmost seat on ties, and for an even run, integer division picks the left middle.

## 11. Interview tips & follow-ups (1:35) — `slides/11.png`

Clarify that both ends are occupied. A follow-up seats people one after another, which calls for a heap of gaps.

## 12. Recap (1:44) — `slides/12.png`

To recap Best Seat: The best seat is the middle of the longest run of empty seats between occupied ones. Try re-implementing it from scratch without looking.
