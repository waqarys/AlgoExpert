# AlgoExpert · Best Seat

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Best Seat (0:00) — `slides/01.png`

Let's solve Best Seat, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. A row of seats (1 taken, 0 free; both ends taken). Return the index of the free seat with the most space on both sides (centre of the widest gap, leftmost on ties), or -1.

## 3. Intuition (0:25) — `slides/03.png`

The best seat is the middle of the longest run of empty seats between occupied ones.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, scan for runs of zeros between ones. Second, track the longest run. Third, return its middle index, or minus one if none.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with best seat. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:54) — `slides/07.png`

To recap Best Seat: The best seat is the middle of the longest run of empty seats between occupied ones. Try re-implementing it from scratch without looking.
