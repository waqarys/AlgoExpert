# AlgoExpert · Phone Number Mnemonics

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Phone Number Mnemonics (0:00) — `slides/01.png`

Let's solve Phone Number Mnemonics, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. All letter strings a digit string could spell on a keypad (0 and 1 map to themselves).

## 3. Intuition (0:19) — `slides/03.png`

Each digit maps to a few letters; explore every combination with backtracking.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

You can expand a list of partial strings digit by digit, or backtrack depth first with one string builder. Both are bounded by four to the n times n, the size of the output.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, recurse digit by digit. Second, try each letter for the digit. Third, at the end, record the word.

## 6. Worked example (0:47) — `slides/06.png`

For one-nine-zero-five, one and zero map to themselves, nine to w, x, y, z, and five to j, k, l.

## 7. Worked example (0:55) — `slides/07.png`

Recursion picks one letter per digit, depth first, then backtracks to try the next letter.

## 8. Worked example (1:01) — `slides/08.png`

In total there are 12 mnemonics: one times four times one times three.

## 9. Java solution (1:07) — `slides/09.png`

Build recurses on the digit index. At the end it records the string; otherwise for each letter of the current key it appends, recurses and removes the letter.

## 10. Complexity (1:17) — `slides/10.png`

Time is O of 4 to the n times n. Space is O of 4 to the n times n.

## 11. Edge cases & pitfalls (1:22) — `slides/11.png`

In this version zero and one map to themselves. Remove the last character after each recursive call.

## 12. Interview tips & follow-ups (1:30) — `slides/12.png`

State the output-size bound clearly. Restricting to real words is a nice trie follow-up.

## 13. Recap (1:37) — `slides/13.png`

To recap Phone Number Mnemonics: Each digit maps to a few letters; explore every combination with backtracking. Try re-implementing it from scratch without looking.
