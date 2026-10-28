# AlgoExpert · Semordnilap

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Semordnilap (0:00) — `slides/01.png`

Let's solve Semordnilap, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return pairs of distinct words where one is the reverse of the other.

## 3. Intuition (0:17) — `slides/03.png`

A word and its reverse form a pair; a hash set finds each partner in constant time.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, put all words in a set. Second, for each word, check whether its reverse is present and different. Third, record the pair and remove both.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with semordnilap. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is O of n times m. Space is O of n times m.

## 7. Recap (0:47) — `slides/07.png`

To recap Semordnilap: A word and its reverse form a pair; a hash set finds each partner in constant time. Try re-implementing it from scratch without looking.
