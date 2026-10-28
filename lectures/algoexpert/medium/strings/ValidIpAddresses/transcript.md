# AlgoExpert · Valid Ip Addresses

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Valid Ip Addresses (0:00) — `slides/01.png`

Let's solve Valid Ip Addresses, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. All ways to insert three dots into a digit string to form valid IPv4 addresses (each part 0-255, no leading zeros).

## 3. Intuition (0:22) — `slides/03.png`

Place three dots; each of the four parts must be 0 to 255 with no leading zeros.

## 4. Brute force vs optimal (0:29) — `slides/04.png`

There are at most twenty-seven ways to place three dots, so brute force is already constant time. The work is validating each part.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, try all positions for three dots. Second, validate each part. Third, collect valid addresses.

## 6. Worked example (0:48) — `slides/06.png`

Place three dots. Each part must be one to three digits, at most 255, with no leading zero.

## 7. Worked example (0:56) — `slides/07.png`

Parts like zero one are invalid because of the leading zero, but a single zero is fine.

## 8. Worked example (1:02) — `slides/08.png`

In total there are 11 valid addresses for one-nine-two-one-six-eight-zero.

## 9. Java solution (1:08) — `slides/09.png`

Three nested loops choose the dot positions, limited to three digits per part. Each split is kept if all four parts pass valid, which checks length, leading zero and the 255 limit.

## 10. Complexity (1:20) — `slides/10.png`

Time is constant (bounded by 3^3 splits). Space is constant.

## 11. Edge cases & pitfalls (1:26) — `slides/11.png`

Watch for leading zeros and parts over 255.

## 12. Interview tips & follow-ups (1:31) — `slides/12.png`

Explain why brute force is bounded and fine here.

## 13. Recap (1:35) — `slides/13.png`

To recap Valid Ip Addresses: Place three dots; each of the four parts must be 0 to 255 with no leading zeros. Try re-implementing it from scratch without looking.
