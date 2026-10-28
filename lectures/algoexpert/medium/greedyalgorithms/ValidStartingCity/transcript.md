# AlgoExpert · Valid Starting City

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Valid Starting City (0:00) — `slides/01.png`

Let's solve Valid Starting City, a medium greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Circular route; city i has fuel i gallons and is distances i miles from the next. Return the unique start index allowing a full loop. The start is the point after the lowest fuel balance.

## 3. Intuition (0:26) — `slides/03.png`

The valid start is right after the point where the running fuel balance is lowest.

## 4. Brute force vs optimal (0:32) — `slides/04.png`

Simulating the trip from every city is quadratic. Instead, run the trip once from city zero, allowing negative fuel. The city where the running total hits its minimum is the right start: starting there, the tank never dips below zero.

## 5. Approach (0:47) — `slides/05.png`

Step by step. First, track miles remaining around the loop. Second, find the city with the minimum balance. Third, that city is the start.

## 6. Worked example (0:59) — `slides/06.png`

Arriving at city 1, starting from city zero, we'd have 5 miles of fuel. The lowest point so far is at city 0.

## 7. Worked example (1:07) — `slides/07.png`

Arriving at city 2, starting from city zero, we'd have 0 miles of fuel. The lowest point so far is at city 0.

## 8. Worked example (1:16) — `slides/08.png`

Arriving at city 3, starting from city zero, we'd have -5 miles of fuel. The lowest point so far is at city 3.

## 9. Worked example (1:25) — `slides/09.png`

Arriving at city 4, starting from city zero, we'd have -15 miles of fuel. The lowest point so far is at city 4.

## 10. Java solution (1:34) — `slides/10.png`

We track miles remaining, the minimum and its city. For each city from one, add the fuel from the previous city times mpg minus the distance, and update the minimum and start.

## 11. Complexity (1:45) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:49) — `slides/12.png`

Remember to multiply fuel by miles per gallon, and choose the city where you arrive with the least fuel.

## 13. Interview tips & follow-ups (1:56) — `slides/13.png`

This is the gas station problem. Explain the minimum-point argument: shifting the start shifts the whole curve up.

## 14. Recap (2:04) — `slides/14.png`

To recap Valid Starting City: The valid start is right after the point where the running fuel balance is lowest. Try re-implementing it from scratch without looking.
