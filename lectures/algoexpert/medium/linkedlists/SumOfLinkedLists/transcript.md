# AlgoExpert · Sum Of Linked Lists

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sum Of Linked Lists (0:00) — `slides/01.png`

Let's solve Sum Of Linked Lists, a medium linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Lists store digits least-significant first; return their sum in the same format.

## 3. Intuition (0:19) — `slides/03.png`

Add digit by digit like grade school, carrying into the next node.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Converting to integers overflows on long lists. Adding digit by digit with a carry, like on paper, works for any length.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, walk both lists together. Second, sum digits plus carry. Third, create a node with the ones digit. Fourth, carry the rest.

## 6. Worked example (0:46) — `slides/06.png`

Add 2 and 9 plus the carry: 11. Write 1 and carry 1.

## 7. Worked example (0:52) — `slides/07.png`

Add 4 and 4 plus the carry: 9. Write 9 and carry 0.

## 8. Worked example (0:57) — `slides/08.png`

Add 7 and 5 plus the carry: 12. Write 2 and carry 1.

## 9. Worked example (1:03) — `slides/09.png`

Add 1 and 0 plus the carry: 2. Write 2 and carry 0.

## 10. Java solution (1:08) — `slides/10.png`

We loop while either list or the carry remains, compute the sum, append its last digit, keep the carry, and advance the lists. Return dummy's next.

## 11. Complexity (1:18) — `slides/11.png`

Time is O of max(n, m). Space is O of max(n, m).

## 12. Edge cases & pitfalls (1:24) — `slides/12.png`

Don't forget the final carry, which may add a new node. Treat a finished list as zeros.

## 13. Interview tips & follow-ups (1:31) — `slides/13.png`

If digits are stored most significant first, reverse the lists or use stacks.

## 14. Recap (1:37) — `slides/14.png`

To recap Sum Of Linked Lists: Add digit by digit like grade school, carrying into the next node. Try re-implementing it from scratch without looking.
