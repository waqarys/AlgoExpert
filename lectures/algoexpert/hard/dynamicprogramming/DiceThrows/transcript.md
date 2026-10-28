# AlgoExpert · Dice Throws

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Dice Throws (0:00) — `slides/01.png`

Let's solve Dice Throws, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Number of ways to roll numDice dice with numSides sides to total target.

## 3. Intuition (0:19) — `slides/03.png`

Count ways to reach each total with dice added one at a time.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, ways for total zero with no dice is one. Second, for each die, roll every face. Third, shift counts forward. Fourth, read ways of target.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with dice throws. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of d times t times s. Space is O of t.

## 7. Recap (0:49) — `slides/07.png`

To recap Dice Throws: Count ways to reach each total with dice added one at a time. Try re-implementing it from scratch without looking.
