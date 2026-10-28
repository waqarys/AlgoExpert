# AlgoExpert · Run Length Encoding

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Run Length Encoding (0:00) — `slides/01.png`

Let's solve Run Length Encoding, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Encode runs as count plus char, with runs longer than 9 split ("AAAAAAAAAAAA" to "9A3A").

## 3. Intuition (0:19) — `slides/03.png`

Count runs of equal characters, but cap each run at nine so the count is always a single digit.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, scan with a running count. Second, flush when the character changes or the count hits nine. Third, write count then character.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with run length encoding. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:48) — `slides/07.png`

To recap Run Length Encoding: Count runs of equal characters, but cap each run at nine so the count is always a single digit. Try re-implementing it from scratch without looking.
