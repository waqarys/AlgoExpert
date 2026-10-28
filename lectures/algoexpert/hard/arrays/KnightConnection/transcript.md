# AlgoExpert · Knight Connection

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Knight Connection (0:00) — `slides/01.png`

Let's solve Knight Connection, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Two knights on an infinite board move alternately or together; minimum number of turns for them to meet equals ceil(knight-move distance / 2). BFS from one knight to the other.

## 3. Intuition (0:24) — `slides/03.png`

Knights cover two cells per joint turn, so compute the minimum knight moves to close the gap, then halve it rounding up.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Searching over both knights' positions squares the state space. Instead, BFS from one knight to the other, then halve the distance, rounding up, since both move each turn.

## 5. Approach (0:42) — `slides/05.png`

Step by step. First, bFS knight moves from the origin to the offset between knights. Second, count moves needed. Third, answer is ceiling of moves over two.

## 6. Worked example (0:54) — `slides/06.png`

After 0 combined knight moves from the first knight, we've reached 1 new squares.

## 7. Worked example (1:00) — `slides/07.png`

After 1 combined knight moves from the first knight, we've reached 8 new squares.

## 8. Worked example (1:05) — `slides/08.png`

After 2 combined knight moves from the first knight, we've reached 8 new squares.

## 9. Worked example (1:11) — `slides/09.png`

We reach the second knight after 2 single-knight moves. Since both knights move each turn, they meet in 1 turns.

## 10. Java solution (1:18) — `slides/10.png`

We BFS from the first knight, storing x, y and distance. When we dequeue the second knight's square, we return distance plus one over two.

## 11. Complexity (1:28) — `slides/11.png`

Time is O of d squared for distance d. Space is O of d squared.

## 12. Edge cases & pitfalls (1:33) — `slides/12.png`

Round odd distances up. The board is infinite, so a seen set is essential.

## 13. Interview tips & follow-ups (1:40) — `slides/13.png`

Bidirectional BFS from both knights would explore far fewer squares.

## 14. Recap (1:45) — `slides/14.png`

To recap Knight Connection: Knights cover two cells per joint turn, so compute the minimum knight moves to close the gap, then halve it rounding up. Try re-implementing it from scratch without looking.
