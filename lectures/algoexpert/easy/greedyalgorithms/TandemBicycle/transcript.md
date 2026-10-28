# AlgoExpert · Tandem Bicycle

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Tandem Bicycle (0:00) — `slides/01.png`

Let's solve Tandem Bicycle, an easy greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Pair red and blue riders; a tandem's speed is the max of its riders. Return the max (fastest equals true) or min possible total speed.

## 3. Intuition (0:23) — `slides/03.png`

Speed is the max of the two riders. For maximum total, pair the fastest with the slowest; for minimum, pair like with like.

## 4. Brute force vs optimal (0:32) — `slides/04.png`

Trying all pairings is factorial. Since each pair counts only its faster rider, the fastest total wastes as few fast riders as possible: pair each fast rider with a slow one. For the slowest total, pair fast with fast.

## 5. Approach (0:46) — `slides/05.png`

Step by step. First, sort both lists. Second, for fastest total, pair one ascending with the other descending. Third, for slowest, pair in the same order. Fourth, sum the max of each pair.

## 6. Worked example (1:02) — `slides/06.png`

Pair red 2 with blue 7. The tandem goes at the faster speed, 7, so the total becomes 7.

## 7. Worked example (1:09) — `slides/07.png`

Pair red 5 with blue 3. The tandem goes at the faster speed, 5, so the total becomes 18.

## 8. Worked example (1:17) — `slides/08.png`

Pair red 9 with blue 1. The tandem goes at the faster speed, 9, so the total becomes 32.

## 9. Java solution (1:25) — `slides/09.png`

We sort both arrays. If we want the fastest total, we read one of them backwards. Then for each index we add the max of the two speeds.

## 10. Complexity (1:35) — `slides/10.png`

Time is O of n log n. Space is constant.

## 11. Edge cases & pitfalls (1:39) — `slides/11.png`

The fastest flag decides whether one list is reversed. Sorting mutates the inputs, so mention it or copy.

## 12. Interview tips & follow-ups (1:48) — `slides/12.png`

Justify the pairing with an exchange argument, and be ready to discuss bikes with more riders.

## 13. Recap (1:54) — `slides/13.png`

To recap Tandem Bicycle: Speed is the max of the two riders. For maximum total, pair the fastest with the slowest; for minimum, pair like with like. Try re-implementing it from scratch without looking.
