# AlgoExpert · Run Length Encoding

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Run Length Encoding (0:00) — `slides/01.png`

Let's solve Run Length Encoding, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Encode runs as count plus char, with runs longer than 9 split ("AAAAAAAAAAAA" to "9A3A").

## 3. Intuition (0:19) — `slides/03.png`

Count runs of equal characters, but cap each run at nine so the count is always a single digit.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Concatenating strings in a loop is quadratic in Java. A single pass with a string builder is linear. The twist is capping runs at nine, so the encoded counts are always a single digit and decoding stays unambiguous.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, scan with a running count. Second, flush when the character changes or the count hits nine. Third, write count then character.

## 6. Worked example (0:52) — `slides/06.png`

The run of A ends because it hit nine, so we write 9 A.

## 7. Worked example (0:56) — `slides/07.png`

The run of A ends, so we write 3 A.

## 8. Worked example (1:00) — `slides/08.png`

The run of B ends, so we write 2 B.

## 9. Worked example (1:04) — `slides/09.png`

The run of C ends, so we write 4 C.

## 10. Worked example (1:08) — `slides/10.png`

The run of D ends, so we write 2 D.

## 11. Java solution (1:11) — `slides/11.png`

We scan from index one, counting the current run. When the character changes or the run reaches nine, we append the count and the previous character, then reset. After the loop we flush the final run.

## 12. Complexity (1:24) — `slides/12.png`

Time is O of n. Space is O of n.

## 13. Edge cases & pitfalls (1:28) — `slides/13.png`

Twelve A's must become nine A three A, not twelve A. And don't forget to flush the last run after the loop.

## 14. Interview tips & follow-ups (1:36) — `slides/14.png`

Explain why the cap avoids ambiguity, and be ready to write the decoder.

## 15. Recap (1:41) — `slides/15.png`

To recap Run Length Encoding: Count runs of equal characters, but cap each run at nine so the count is always a single digit. Try re-implementing it from scratch without looking.
