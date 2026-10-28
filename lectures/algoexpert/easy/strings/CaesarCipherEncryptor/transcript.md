# AlgoExpert · Caesar Cipher Encryptor

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Caesar Cipher Encryptor (0:00) — `slides/01.png`

Let's solve Caesar Cipher Encryptor, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Shift each lowercase letter by key positions, wrapping around z.

## 3. Intuition (0:18) — `slides/03.png`

Shift each letter by the key, wrapping around the alphabet with modulo twenty-six.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, reduce the key modulo twenty-six. Second, for each letter, compute its new code. Third, wrap past z back to a. Fourth, build the new string.

## 5. Java solution (0:33) — `slides/05.png`

Here's the Java solution, starting with caesar cypher encryptor. It follows the steps we just described.

## 6. Complexity (0:41) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:44) — `slides/07.png`

To recap Caesar Cipher Encryptor: Shift each letter by the key, wrapping around the alphabet with modulo twenty-six. Try re-implementing it from scratch without looking.
