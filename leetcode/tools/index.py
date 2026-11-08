#!/usr/bin/env python3
"""Regenerate leetcode/README.md from content/*/explanation.md."""
import os, re, glob
LC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows, cats = [], {}
for md in sorted(glob.glob(os.path.join(LC, "content", "*", "explanation.md"))):
    t = open(md).read(); slug = os.path.basename(os.path.dirname(md))
    title = re.search(r"^# (.+)$", t, re.M).group(1)
    diff, cat, url = re.search(r"Difficulty:\*\* (\w+) \| \*\*Category:\*\* (.+?) \| \*\*LeetCode:\*\* (\S+)", t).groups()
    src = re.search(r"```java file=(\S+)", t).group(1)
    cats.setdefault(cat, []).append(f"| {title} | {diff} | [LeetCode]({url}) | [Explanation](content/{slug}/explanation.md) | [Slides PDF](content/{slug}/slides.pdf) · [PNGs](content/{slug}/slides/) | [Java](java/src/main/java/{src}) |")
order = ["Arrays & Hashing", "Two Pointers", "Sliding Window", "Stack", "Binary Search", "Linked List", "Trees", "Tries",
         "Heap / Priority Queue", "Backtracking", "Graphs", "Advanced Graphs", "1-D Dynamic Programming",
         "2-D Dynamic Programming", "Greedy", "Intervals", "Math & Geometry", "Bit Manipulation"]
n = sum(len(v) for v in cats.values())
out = [f"""# LeetCode: NeetCode 150 in Java (Build with Waqar)

Interview-focused LeetCode set: the **NeetCode 150** list (a superset of Blind 75), solved in Java 17 with
JUnit 5 tests, plus an explanation, video script, and 1920x1080 dark slides for every problem.
**{n} problems done so far.**

The problem list comes from [neetcode-gh/leetcode](https://github.com/neetcode-gh/leetcode) (MIT).
All code, explanations and slides here are original.

## Layout
- `java/`: Maven module. `src/main/java/<category>/<Problem>.java` holds the solution, with a Javadoc header for
  the summary, approach and complexity. `src/test/java/...` holds the tests. Run `cd leetcode/java && mvn test`.
- `content/<NNNN-slug>/explanation.md`: problem, intuition, brute force, optimal approach, worked trace,
  complexity, pitfalls, video script, solution and tests. This is the single source of truth.
- `content/<NNNN-slug>/slides/NN.png` + `slides.pdf`: ready for OBS / CapCut.
- `tools/build.py`: extracts the Java from the markdown (`python tools/build.py`) and renders the slides (`--slides`).
  It reuses `lectures/pipeline/make_lecture.py` for the visual style. `tools/index.py` rebuilds this README.
- The older files in `leetcode/pom.xml` and `leetcode/src/` are untouched.
"""]
for c in order + [c for c in cats if c not in order]:
    if c not in cats: continue
    out.append(f"\n## {c} ({len(cats[c])})\n\n| Problem | Difficulty | Link | Explanation | Slides | Code |\n|---|---|---|---|---|---|")
    out += cats[c]
open(os.path.join(LC, "README.md"), "w").write("\n".join(out) + "\n")
print(n)
