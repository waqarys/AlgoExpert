# AlgoExpert · Merging Linked Lists

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merging Linked Lists (0:00) — `slides/01.png`

Let's solve Merging Linked Lists, a medium linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Two lists may converge into a shared tail; return the first shared node or null. Two pointers that switch lists meet at the junction after at most n plus m steps.

## 3. Intuition (0:24) — `slides/03.png`

Two pointers that switch to the other list after finishing travel the same distance and meet at the junction.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

Comparing every pair is quadratic. A hash set of A's nodes is linear but uses memory. Two pointers that switch to the other list at the end both travel the same total distance, so they meet at the intersection with constant space.

## 5. Approach (0:45) — `slides/05.png`

Step by step. First, advance both pointers. Second, when one ends, jump to the other list's head. Third, they meet at the shared node or both null.

## 6. Worked example (0:57) — `slides/06.png`

The two lists merge at the node with value one and share everything after it.

## 7. Worked example (1:02) — `slides/07.png`

After 0 steps, p is at 2 and q is at 8.

## 8. Worked example (1:06) — `slides/08.png`

After 2 steps, p is at 1 and q is at 1.

## 9. Worked example (1:10) — `slides/09.png`

After 5 steps, p is at 8 and q is at 2.

## 10. Worked example (1:15) — `slides/10.png`

After 7 steps, p is at 1 and q is at 1.

## 11. Worked example (1:19) — `slides/11.png`

Each pointer travels the length of both lists, so they line up and meet at the shared node.

## 12. Java solution (1:25) — `slides/12.png`

Two pointers start at each head. While they differ, each moves to next, or to the other list's head when it hits null. Return either.

## 13. Complexity (1:35) — `slides/13.png`

Time is O of n plus m. Space is constant.

## 14. Edge cases & pitfalls (1:39) — `slides/14.png`

Compare node references, not values; two different nodes can share a value. With no intersection, both reach null together and we return null.

## 15. Interview tips & follow-ups (1:48) — `slides/15.png`

Explain the equal-distance argument, and mention aligning by length difference as an alternative.

## 16. Recap (1:55) — `slides/16.png`

To recap Merging Linked Lists: Two pointers that switch to the other list after finishing travel the same distance and meet at the junction. Try re-implementing it from scratch without looking.
