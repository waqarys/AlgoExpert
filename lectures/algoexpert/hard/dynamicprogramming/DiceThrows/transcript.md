# AlgoExpert · Dice Throws

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Dice Throws (0:00) — `slides/01.png`

Let's solve Dice Throws, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Number of ways to roll numDice dice with numSides sides to total target.

## 3. Intuition (0:19) — `slides/03.png`

Count ways to reach each total with dice added one at a time.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Trying every face combination is sides to the power dice. A DP over number of dice and total counts them in dice times target times sides.

## 5. Approach (0:32) — `slides/05.png`

Step by step. First, ways for total zero with no dice is one. Second, for each die, roll every face. Third, shift counts forward. Fourth, read ways of target.

## 6. Worked example (0:47) — `slides/06.png`

With zero dice, there's one way to make a total of zero.

## 7. Worked example (0:51) — `slides/07.png`

Adding die 1, each total spreads to the next one to six totals. Now there are 0 ways to make seven.

## 8. Worked example (0:59) — `slides/08.png`

Adding die 2, each total spreads to the next one to six totals. Now there are 6 ways to make seven.

## 9. Java solution (1:07) — `slides/09.png`

Ways starts with one at zero. For each die, a new array spreads every reachable total to total plus one through total plus sides. Return ways of target.

## 10. Complexity (1:18) — `slides/10.png`

Time is O of d times t times s. Space is O of t.

## 11. Edge cases & pitfalls (1:23) — `slides/11.png`

Targets below the number of dice or above dice times sides have zero ways.

## 12. Interview tips & follow-ups (1:28) — `slides/12.png`

Dividing by sides to the dice gives the probability.

## 13. Recap (1:32) — `slides/13.png`

To recap Dice Throws: Count ways to reach each total with dice added one at a time. Try re-implementing it from scratch without looking.
