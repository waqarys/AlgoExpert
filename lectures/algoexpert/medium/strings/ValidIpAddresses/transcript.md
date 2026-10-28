# AlgoExpert · Valid Ip Addresses

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Valid Ip Addresses (0:00) — `slides/01.png`

Let's solve Valid Ip Addresses, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. All ways to insert three dots into a digit string to form valid IPv4 addresses (each part 0-255, no leading zeros).

## 3. Intuition (0:22) — `slides/03.png`

Place three dots; each of the four parts must be 0 to 255 with no leading zeros.

## 4. Approach (0:29) — `slides/04.png`

Step by step. First, try all positions for three dots. Second, validate each part. Third, collect valid addresses.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with valid ip addresses. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is constant (bounded by 3^3 splits). Space is constant.

## 7. Recap (0:54) — `slides/07.png`

To recap Valid Ip Addresses: Place three dots; each of the four parts must be 0 to 255 with no leading zeros. Try re-implementing it from scratch without looking.
