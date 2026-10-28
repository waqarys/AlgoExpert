# AlgoExpert · Phone Number Mnemonics

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Phone Number Mnemonics (0:00) — `slides/01.png`

Let's solve Phone Number Mnemonics, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. All letter strings a digit string could spell on a keypad (0 and 1 map to themselves).

## 3. Intuition (0:19) — `slides/03.png`

Each digit maps to a few letters; explore every combination with backtracking.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, recurse digit by digit. Second, try each letter for the digit. Third, at the end, record the word.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with phone number mnemonics. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of 4 to the n times n. Space is O of 4 to the n times n.

## 7. Recap (0:49) — `slides/07.png`

To recap Phone Number Mnemonics: Each digit maps to a few letters; explore every combination with backtracking. Try re-implementing it from scratch without looking.
