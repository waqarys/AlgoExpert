# AlgoExpert · Calendar Matching

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Calendar Matching (0:00) — `slides/01.png`

Let's solve Calendar Matching, a very hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Two people's meetings ("HH:MM" pairs) and daily bounds; return all free slots of at least duration minutes available to both. Convert to minutes, merge busy intervals, invert.

## 3. Intuition (0:25) — `slides/03.png`

Merge both calendars, including bounds as meetings, then gaps of the right length are free slots.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, convert times to minutes. Second, add each person's bounds as blocked time. Third, sort and merge meetings. Fourth, return gaps at least duration long.

## 5. Java solution (1/2) (0:46) — `slides/05.png`

Here's the Java solution, starting with calendar matching. It follows the steps we just described.

## 6. Java solution (2/2) (0:53) — `slides/06.png`

Continuing with add cal, min, fmt.

## 7. Complexity (0:57) — `slides/07.png`

Time is O of c1 plus c2. Space is O of c1 plus c2.

## 8. Recap (1:03) — `slides/08.png`

To recap Calendar Matching: Merge both calendars, including bounds as meetings, then gaps of the right length are free slots. Try re-implementing it from scratch without looking.
