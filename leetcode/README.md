# LeetCode: NeetCode 150 in Java (Build with Waqar)

Interview-focused LeetCode set: the **NeetCode 150** list (a superset of Blind 75), solved in Java 17 with
JUnit 5 tests, plus an explanation, video script, and 1920x1080 dark slides for every problem.
**9 problems done so far.**

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


## Arrays & Hashing (9)

| Problem | Difficulty | Link | Explanation | Slides | Code |
|---|---|---|---|---|---|
| 0001. Two Sum | Easy | [LeetCode](https://leetcode.com/problems/two-sum/) | [Explanation](content/0001-two-sum/explanation.md) | [Slides PDF](content/0001-two-sum/slides.pdf) · [PNGs](content/0001-two-sum/slides/) | [Java](java/src/main/java/arrays/TwoSum.java) |
| 0036. Valid Sudoku | Medium | [LeetCode](https://leetcode.com/problems/valid-sudoku/) | [Explanation](content/0036-valid-sudoku/explanation.md) | [Slides PDF](content/0036-valid-sudoku/slides.pdf) · [PNGs](content/0036-valid-sudoku/slides/) | [Java](java/src/main/java/arrays/ValidSudoku.java) |
| 0049. Group Anagrams | Medium | [LeetCode](https://leetcode.com/problems/group-anagrams/) | [Explanation](content/0049-group-anagrams/explanation.md) | [Slides PDF](content/0049-group-anagrams/slides.pdf) · [PNGs](content/0049-group-anagrams/slides/) | [Java](java/src/main/java/arrays/GroupAnagrams.java) |
| 0128. Longest Consecutive Sequence | Medium | [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/) | [Explanation](content/0128-longest-consecutive-sequence/explanation.md) | [Slides PDF](content/0128-longest-consecutive-sequence/slides.pdf) · [PNGs](content/0128-longest-consecutive-sequence/slides/) | [Java](java/src/main/java/arrays/LongestConsecutiveSequence.java) |
| 0217. Contains Duplicate | Easy | [LeetCode](https://leetcode.com/problems/contains-duplicate/) | [Explanation](content/0217-contains-duplicate/explanation.md) | [Slides PDF](content/0217-contains-duplicate/slides.pdf) · [PNGs](content/0217-contains-duplicate/slides/) | [Java](java/src/main/java/arrays/ContainsDuplicate.java) |
| 0238. Product of Array Except Self | Medium | [LeetCode](https://leetcode.com/problems/product-of-array-except-self/) | [Explanation](content/0238-product-of-array-except-self/explanation.md) | [Slides PDF](content/0238-product-of-array-except-self/slides.pdf) · [PNGs](content/0238-product-of-array-except-self/slides/) | [Java](java/src/main/java/arrays/ProductOfArrayExceptSelf.java) |
| 0242. Valid Anagram | Easy | [LeetCode](https://leetcode.com/problems/valid-anagram/) | [Explanation](content/0242-valid-anagram/explanation.md) | [Slides PDF](content/0242-valid-anagram/slides.pdf) · [PNGs](content/0242-valid-anagram/slides/) | [Java](java/src/main/java/arrays/ValidAnagram.java) |
| 0271. Encode and Decode Strings | Medium | [LeetCode](https://leetcode.com/problems/encode-and-decode-strings/) | [Explanation](content/0271-encode-and-decode-strings/explanation.md) | [Slides PDF](content/0271-encode-and-decode-strings/slides.pdf) · [PNGs](content/0271-encode-and-decode-strings/slides/) | [Java](java/src/main/java/arrays/EncodeAndDecodeStrings.java) |
| 0347. Top K Frequent Elements | Medium | [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) | [Explanation](content/0347-top-k-frequent-elements/explanation.md) | [Slides PDF](content/0347-top-k-frequent-elements/slides.pdf) · [PNGs](content/0347-top-k-frequent-elements/slides/) | [Java](java/src/main/java/arrays/TopKFrequentElements.java) |
