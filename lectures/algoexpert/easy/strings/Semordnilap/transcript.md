# AlgoExpert · Semordnilap

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Semordnilap (0:00) — `slides/01.png`

Let's solve Semordnilap, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return pairs of distinct words where one is the reverse of the other.

## 3. Intuition (0:17) — `slides/03.png`

A word and its reverse form a pair; a hash set finds each partner in constant time.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Comparing every pair of words is quadratic. With a hash set, each word checks for its reverse in constant time, so the whole thing is linear in the total characters.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, put all words in a set. Second, for each word, check whether its reverse is present and different. Third, record the pair and remove both.

## 6. Worked example (0:46) — `slides/06.png`

The reverse of diaper is repaid, which is in the set. Record the pair and remove both so it isn't counted twice.

## 7. Worked example (0:54) — `slides/07.png`

The reverse of abc is cba, which is in the set. Record the pair and remove both so it isn't counted twice.

## 8. Worked example (1:03) — `slides/08.png`

The reverse of test, tset, isn't in the list.

## 9. Java solution (1:07) — `slides/09.png`

We put all words in a set. For each word, we reverse it; if the reverse is in the set and differs from the word, we add the pair and remove both words.

## 10. Complexity (1:17) — `slides/10.png`

Time is O of n times m. Space is O of n times m.

## 11. Edge cases & pitfalls (1:21) — `slides/11.png`

A palindrome would match itself, so skip that case. Removing matched words prevents duplicate pairs.

## 12. Interview tips & follow-ups (1:29) — `slides/12.png`

Follow-ups include counting pairs or handling duplicate words.

## 13. Recap (1:34) — `slides/13.png`

To recap Semordnilap: A word and its reverse form a pair; a hash set finds each partner in constant time. Try re-implementing it from scratch without looking.
