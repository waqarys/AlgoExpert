# AlgoExpert · Powerset

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Powerset (0:00) — `slides/01.png`

Let's solve Powerset, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Every subset of a set of distinct ints (iteratively doubling).

## 3. Intuition (0:18) — `slides/03.png`

Each new element doubles the subsets: every existing subset with or without it.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Each subset corresponds to an n-bit mask, so there are two to the n of them. Iteratively doubling the list, or recursion, produces them all in n times two to the n.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, start with the empty set. Second, for each element, copy all subsets and add it. Third, return all.

## 6. Worked example (0:46) — `slides/06.png`

Start with just the empty subset.

## 7. Worked example (0:49) — `slides/07.png`

For 1, copy every existing subset and add 1 to the copy. That doubles the count to 2.

## 8. Worked example (0:57) — `slides/08.png`

For 2, copy every existing subset and add 2 to the copy. That doubles the count to 4.

## 9. Worked example (1:04) — `slides/09.png`

For 3, copy every existing subset and add 3 to the copy. That doubles the count to 8.

## 10. Java solution (1:11) — `slides/10.png`

We start with one empty subset. For each value, we take the current size and, for each existing subset, add a copy with the value appended.

## 11. Complexity (1:21) — `slides/11.png`

Time is O of n times 2 to the n. Space is O of n times 2 to the n.

## 12. Edge cases & pitfalls (1:26) — `slides/12.png`

Capture the list size before the inner loop, or you'll loop forever on subsets you just added. Remember the empty set.

## 13. Interview tips & follow-ups (1:34) — `slides/13.png`

Mention the bitmask view. Follow-ups handle duplicates or restrict to a target sum.

## 14. Recap (1:41) — `slides/14.png`

To recap Powerset: Each new element doubles the subsets: every existing subset with or without it. Try re-implementing it from scratch without looking.
