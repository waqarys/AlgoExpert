# AlgoExpert · Valid Starting City

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Valid Starting City (0:00) — `slides/01.png`

Let's solve Valid Starting City, a medium greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Circular route; city i has fuel i gallons and is distances i miles from the next. Return the unique start index allowing a full loop. The start is the point after the lowest fuel balance.

## 3. Intuition (0:26) — `slides/03.png`

The valid start is right after the point where the running fuel balance is lowest.

## 4. Approach (0:32) — `slides/04.png`

Step by step. First, track miles remaining around the loop. Second, find the city with the minimum balance. Third, that city is the start.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with valid starting city. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:55) — `slides/07.png`

To recap Valid Starting City: The valid start is right after the point where the running fuel balance is lowest. Try re-implementing it from scratch without looking.
