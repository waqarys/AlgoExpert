# AlgoExpert · Product Sum

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Product Sum (0:00) — `slides/01.png`

Let's solve Product Sum, an easy recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. A "special" array holds ints or nested special arrays; each nested array's sum is multiplied by its depth (outermost equals 1).

## 3. Intuition (0:21) — `slides/03.png`

A nested array's sum is multiplied by its depth, which is naturally recursive.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

There's no shortcut: every element must be visited once. The key is where the multiplication happens. Each list sums its elements, including nested results, and multiplies once by its own depth.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, sum the elements at this level. Second, for a nested list, recurse with depth plus one. Third, multiply the level sum by the depth. Fourth, return it.

## 6. Worked example (0:55) — `slides/06.png`

At depth one, we add the plain numbers five, two and three, and recurse into each nested list.

## 7. Worked example (1:01) — `slides/07.png`

The list seven, minus one sums to six. It's at depth two, so it contributes twelve.

## 8. Worked example (1:08) — `slides/08.png`

The innermost list sums to minus five, times depth three gives minus fifteen.

## 9. Worked example (1:14) — `slides/09.png`

Back in the list six, the inner list, four: that's six minus fifteen plus four, minus five, times two, minus ten.

## 10. Worked example (1:21) — `slides/10.png`

At the top: five plus two plus twelve plus three minus ten is twelve, times depth one. The answer is twelve.

## 11. Java solution (1:29) — `slides/11.png`

We loop over the list. Integers are added directly. Nested lists recurse with depth plus one. At the end we multiply the sum by the current depth.

## 12. Complexity (1:41) — `slides/12.png`

Time is O of n total elements. Space is O of d depth.

## 13. Edge cases & pitfalls (1:47) — `slides/13.png`

Empty lists contribute zero. Make sure each nested result is multiplied only by its own depth, not by every ancestor's.

## 14. Interview tips & follow-ups (1:56) — `slides/14.png`

In Java the input is a list of objects, so you need an instanceof check. A follow-up flips the weighting so deeper lists count less.

## 15. Recap (2:05) — `slides/15.png`

To recap Product Sum: A nested array's sum is multiplied by its depth, which is naturally recursive. Try re-implementing it from scratch without looking.
