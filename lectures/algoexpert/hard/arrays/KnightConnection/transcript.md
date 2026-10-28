# AlgoExpert · Knight Connection

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Knight Connection (0:00) — `slides/01.png`

Let's solve Knight Connection, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Two knights on an infinite board move alternately or together; minimum number of turns for them to meet equals ceil(knight-move distance / 2). BFS from one knight to the other.

## 3. Intuition (0:24) — `slides/03.png`

Knights cover two cells per joint turn, so compute the minimum knight moves to close the gap, then halve it rounding up.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, bFS knight moves from the origin to the offset between knights. Second, count moves needed. Third, answer is ceiling of moves over two.

## 5. Java solution (0:44) — `slides/05.png`

Here's the Java solution, starting with knight connection. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of d squared for distance d. Space is O of d squared.

## 7. Recap (0:56) — `slides/07.png`

To recap Knight Connection: Knights cover two cells per joint turn, so compute the minimum knight moves to close the gap, then halve it rounding up. Try re-implementing it from scratch without looking.
