# AlgoExpert · Four Number Sum

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Four Number Sum (0:00) — `slides/01.png`

Let's solve Four Number Sum, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. All quadruplets of distinct integers summing to target (any order). Store pair sums seen before index i, combine with pairs after i, so each quadruplet is reported once.

## 3. Intuition (0:24) — `slides/03.png`

Split the quadruplet into two pairs, and use a hash map of pair sums seen strictly before index i to avoid duplicates.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Four nested loops is n to the fourth. Fixing two and two-pointering the rest is cubic. Storing pair sums in a hash map gives quadratic average time.

## 5. Approach (0:42) — `slides/05.png`

Step by step. First, for each i, look at pairs i with j after it and check target minus their sum in the map. Second, then add pairs k with i, k before i, to the map. Third, this ordering prevents reusing indices.

## 6. Worked example (0:58) — `slides/06.png`

At index 1, value 6: we look for pairs after it whose sum plus a stored earlier pair makes sixteen, finding nothing yet. Then we store every pair that ends at 6.

## 7. Worked example (1:09) — `slides/07.png`

At index 2, value 4: we look for pairs after it whose sum plus a stored earlier pair makes sixteen, finding [[7, 6, 4, -1]]. Then we store every pair that ends at 4.

## 8. Worked example (1:21) — `slides/08.png`

At index 3, value -1: we look for pairs after it whose sum plus a stored earlier pair makes sixteen, finding nothing yet. Then we store every pair that ends at -1.

## 9. Worked example (1:33) — `slides/09.png`

At index 4, value 1: we look for pairs after it whose sum plus a stored earlier pair makes sixteen, finding [[7, 6, 1, 2]]. Then we store every pair that ends at 1.

## 10. Java solution (1:45) — `slides/10.png`

For each i from one, we look at every j after i and add each stored pair summing to target minus a i minus a j. Then we store all pairs of earlier elements with a i.

## 11. Complexity (1:55) — `slides/11.png`

Time is O of n squared avg. Space is O of n squared.

## 12. Edge cases & pitfalls (2:00) — `slides/12.png`

Add pairs ending at i only after looking ahead from i, so the two halves never overlap and each quadruplet is found once.

## 13. Interview tips & follow-ups (2:07) — `slides/13.png`

The ordering trick is the heart of the solution; explain it. The k-sum generalisation recurses down to two-sum.

## 14. Recap (2:15) — `slides/14.png`

To recap Four Number Sum: Split the quadruplet into two pairs, and use a hash map of pair sums seen strictly before index i to avoid duplicates. Try re-implementing it from scratch without looking.
