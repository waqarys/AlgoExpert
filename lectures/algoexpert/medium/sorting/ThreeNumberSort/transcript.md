# AlgoExpert · Three Number Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Three Number Sort (0:00) — `slides/01.png`

Let's solve Three Number Sort, a medium sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sort an array in place according to a 3-value order (Dutch national flag).

## 3. Intuition (0:18) — `slides/03.png`

Dutch national flag: three regions grown by three pointers in one pass.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, first, second and third pointers. Second, swap firsts to the front. Third, leave seconds. Fourth, swap thirds to the back.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with three number sort. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:48) — `slides/07.png`

To recap Three Number Sort: Dutch national flag: three regions grown by three pointers in one pass. Try re-implementing it from scratch without looking.
