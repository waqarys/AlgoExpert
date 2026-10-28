# AlgoExpert · Node Swap

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Node Swap (0:00) — `slides/01.png`

Let's solve Node Swap, a very hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Swap every pair of adjacent nodes (not values); return the new head.

## 3. Intuition (0:18) — `slides/03.png`

Swap pairs by rewiring three links at a time, using a dummy head.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Swapping values is usually disallowed. Relinking pairs with a dummy head is constant space.

## 5. Approach (0:31) — `slides/05.png`

Step by step. First, dummy before head. Second, for each pair, rewire previous, first and second. Third, advance by two.

## 6. Worked example (0:42) — `slides/06.png`

After 0 swaps. Next, swap 0 and 1 by relinking.

## 7. Worked example (0:48) — `slides/07.png`

After 1 swaps. Next, swap 2 and 3 by relinking.

## 8. Worked example (0:54) — `slides/08.png`

After 2 swaps. Next, swap 4 and 5 by relinking.

## 9. Worked example (1:00) — `slides/09.png`

After 3 swaps. Done.

## 10. Java solution (1:04) — `slides/10.png`

With p at the dummy, while two nodes follow, we relink a and b: a's next to b's next, b's next to a, p's next to b, then move p to a.

## 11. Complexity (1:12) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:16) — `slides/12.png`

An odd final node stays put.

## 13. Interview tips & follow-ups (1:19) — `slides/13.png`

Generalises to reversing in groups of k.

## 14. Recap (1:23) — `slides/14.png`

To recap Node Swap: Swap pairs by rewiring three links at a time, using a dummy head. Try re-implementing it from scratch without looking.
