# AlgoExpert · Majority Element

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Majority Element (0:00) — `slides/01.png`

Let's solve Majority Element, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. An element occurs in more than half the array; find it (Boyer-Moore voting).

## 3. Intuition (0:18) — `slides/03.png`

Boyer-Moore voting: pair off different values; the majority survives the cancellation.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Counting each value separately is quadratic. A hash map is linear but uses memory, and sorting puts the majority in the middle in n log n. Boyer-Moore voting gets linear time with constant space, by letting different values cancel each other out.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, keep a candidate and a count. Second, same value increments, different decrements. Third, when the count hits zero, adopt the current value. Fourth, the final candidate is the answer.

## 6. Worked example (0:55) — `slides/06.png`

Element 1 matches the candidate, so the count goes up. Candidate 1, count 1.

## 7. Worked example (1:02) — `slides/07.png`

Element 2 differs from the candidate, so it cancels one vote. Candidate 1, count 0.

## 8. Worked example (1:09) — `slides/08.png`

Element 3 matches the candidate, so the count goes up. Candidate 3, count 1.

## 9. Worked example (1:16) — `slides/09.png`

Element 2 matches the candidate, so the count goes up. Candidate 2, count 1.

## 10. Worked example (1:23) — `slides/10.png`

Element 1 differs from the candidate, so it cancels one vote. Candidate 2, count 0.

## 11. Worked example (1:30) — `slides/11.png`

Element 2 matches the candidate, so the count goes up. Candidate 2, count 1.

## 12. Java solution (1:37) — `slides/12.png`

We keep a candidate and a count. When the count is zero, the current value becomes the candidate. Then the count goes up for a match and down otherwise. The final candidate is returned.

## 13. Complexity (1:50) — `slides/13.png`

Time is O of n. Space is constant.

## 14. Edge cases & pitfalls (1:54) — `slides/14.png`

This problem guarantees a majority exists. Without that guarantee, you'd need a second pass to verify the candidate.

## 15. Interview tips & follow-ups (2:03) — `slides/15.png`

Explain the intuition: the majority has more votes than everything else combined, so it survives the cancellations. The follow-up finds elements appearing more than n over three times with two candidates.

## 16. Recap (2:15) — `slides/16.png`

To recap Majority Element: Boyer-Moore voting: pair off different values; the majority survives the cancellation. Try re-implementing it from scratch without looking.
