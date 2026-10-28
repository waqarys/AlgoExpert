# AlgoExpert · Generate Div Tags

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Generate Div Tags (0:00) — `slides/01.png`

Let's solve Generate Div Tags, a hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. All valid strings of n matched under div over under /div over pairs (balanced-parentheses generation).

## 3. Intuition (0:21) — `slides/03.png`

Backtracking: you can open a tag while some remain and close one only if more are open than closed.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, track opening and closing tags left. Second, add an opening tag if available. Third, add a closing tag if it keeps balance. Fourth, record complete strings.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with generate div tags. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of Catalan(n) times n. Space is O of Catalan(n) times n.

## 7. Recap (0:55) — `slides/07.png`

To recap Generate Div Tags: Backtracking: you can open a tag while some remain and close one only if more are open than closed. Try re-implementing it from scratch without looking.
