# AlgoExpert · Merge Overlapping Intervals

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merge Overlapping Intervals (0:00) — `slides/01.png`

Let's solve Merge Overlapping Intervals, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Merge all overlapping start, end intervals; result sorted by start.

## 3. Intuition (0:19) — `slides/03.png`

After sorting by start, overlapping intervals are adjacent, so one pass can merge them.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Repeatedly scanning for any overlapping pair is at least quadratic. Once intervals are sorted by start, an interval can only overlap the most recent merged one, so a single sweep finishes the job after an n log n sort.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, sort by start. Second, keep the current merged interval. Third, extend its end on overlap. Fourth, otherwise start a new one.

## 6. Worked example (0:52) — `slides/06.png`

Interval 1 to 2: it starts after the last merged interval ends, so it begins a new one.

## 7. Worked example (0:58) — `slides/07.png`

Interval 3 to 5: it starts after the last merged interval ends, so it begins a new one.

## 8. Worked example (1:04) — `slides/08.png`

Interval 4 to 7: it starts before the last merged interval ends, so we extend that interval's end to 7.

## 9. Worked example (1:11) — `slides/09.png`

Interval 6 to 8: it starts before the last merged interval ends, so we extend that interval's end to 8.

## 10. Worked example (1:18) — `slides/10.png`

Interval 9 to 10: it starts after the last merged interval ends, so it begins a new one.

## 11. Java solution (1:25) — `slides/11.png`

We clone and sort by start. For each interval, if the last merged interval's end reaches its start, we extend that end to the max; otherwise we append a copy.

## 12. Complexity (1:35) — `slides/12.png`

Time is O of n log n. Space is O of n.

## 13. Edge cases & pitfalls (1:39) — `slides/13.png`

Touching endpoints count as overlapping, which is why we compare with greater-or-equal. A contained interval is handled by taking the max of the ends.

## 14. Interview tips & follow-ups (1:49) — `slides/14.png`

Follow-ups include inserting one interval into an already merged list, or counting overlapping meetings.

## 15. Recap (1:55) — `slides/15.png`

To recap Merge Overlapping Intervals: After sorting by start, overlapping intervals are adjacent, so one pass can merge them. Try re-implementing it from scratch without looking.
