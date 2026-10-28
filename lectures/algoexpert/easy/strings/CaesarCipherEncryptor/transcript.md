# AlgoExpert · Caesar Cipher Encryptor

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Caesar Cipher Encryptor (0:00) — `slides/01.png`

Let's solve Caesar Cipher Encryptor, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Shift each lowercase letter by key positions, wrapping around z.

## 3. Intuition (0:18) — `slides/03.png`

Shift each letter by the key, wrapping around the alphabet with modulo twenty-six.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

A naive version steps each letter forward k times. With modular arithmetic, each letter is shifted in one step, and reducing k modulo twenty-six handles huge keys.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, reduce the key modulo twenty-six. Second, for each letter, compute its new code. Third, wrap past z back to a. Fourth, build the new string.

## 6. Worked example (0:49) — `slides/06.png`

The letter x is position 23. Adding 2 and taking modulo twenty-six gives 25, which is z.

## 7. Worked example (0:57) — `slides/07.png`

The letter y is position 24. Adding 2 and taking modulo twenty-six gives 0, which is a.

## 8. Worked example (1:05) — `slides/08.png`

The letter z is position 25. Adding 2 and taking modulo twenty-six gives 1, which is b.

## 9. Java solution (1:13) — `slides/09.png`

We reduce the key modulo twenty-six, then map each character to its zero-based position, add the key, wrap with modulo, and convert back to a character.

## 10. Complexity (1:22) — `slides/10.png`

Time is O of n. Space is O of n.

## 11. Edge cases & pitfalls (1:26) — `slides/11.png`

Remember wrap-around from z back to a and reduce large keys first.

## 12. Interview tips & follow-ups (1:31) — `slides/12.png`

Build the result with a character array or StringBuilder. Follow-ups include decryption and handling uppercase or punctuation.

## 13. Recap (1:40) — `slides/13.png`

To recap Caesar Cipher Encryptor: Shift each letter by the key, wrapping around the alphabet with modulo twenty-six. Try re-implementing it from scratch without looking.
