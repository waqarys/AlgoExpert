# AlgoExpert · Shorten Path

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Shorten Path (0:00) — `slides/01.png`

Let's solve Shorten Path, a hard stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Simplify a Unix path (absolute or relative), resolving "." and ".." and duplicate slashes. Leading ".." are kept for relative paths and dropped at the root of absolute paths.

## 3. Intuition (0:24) — `slides/03.png`

Process path tokens with a stack: dots are ignored, double dots pop, names push.

## 4. Brute force vs optimal (0:29) — `slides/04.png`

Repeated string replacement is fragile. Splitting on slashes and using a stack handles dots and double dots cleanly in linear time.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, split on slashes. Second, skip empty tokens and single dots. Third, double dot pops, or is kept for relative paths. Fourth, join back.

## 6. Worked example (0:53) — `slides/06.png`

Token foo: a directory name, push.

## 7. Worked example (0:57) — `slides/07.png`

Token test: a directory name, push.

## 8. Worked example (1:01) — `slides/08.png`

Token test: a directory name, push.

## 9. Worked example (1:05) — `slides/09.png`

Token ..: go up a directory, pop.

## 10. Worked example (1:08) — `slides/10.png`

Token bar: a directory name, push.

## 11. Worked example (1:12) — `slides/11.png`

Join the stack with slashes: slash foo, bar, baz.

## 12. Java solution (1:17) — `slides/12.png`

We split on slash, skip empty and dot tokens, pop on dot-dot unless the stack is empty or ends in dot-dot (then push it for relative paths), and push names. Join and prefix a slash if absolute.

## 13. Complexity (1:29) — `slides/13.png`

Time is O of n. Space is O of n.

## 14. Edge cases & pitfalls (1:33) — `slides/14.png`

At the root of an absolute path, dot-dot does nothing; in relative paths, leading dot-dots are kept.

## 15. Interview tips & follow-ups (1:40) — `slides/15.png`

This is simplify path.

## 16. Recap (1:43) — `slides/16.png`

To recap Shorten Path: Process path tokens with a stack: dots are ignored, double dots pop, names push. Try re-implementing it from scratch without looking.
