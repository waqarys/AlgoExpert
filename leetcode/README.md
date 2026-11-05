# LeetCode: NeetCode 150 in Java (Build with Waqar)

Interview-focused LeetCode set: the **NeetCode 150** list (a superset of Blind 75), solved in Java 17 with
JUnit 5 tests, plus an explanation, video script, and 1920x1080 dark slides for every problem.
**34 problems done so far.**

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

## Two Pointers (5)

| Problem | Difficulty | Link | Explanation | Slides | Code |
|---|---|---|---|---|---|
| 0011. Container With Most Water | Medium | [LeetCode](https://leetcode.com/problems/container-with-most-water/) | [Explanation](content/0011-container-with-most-water/explanation.md) | [Slides PDF](content/0011-container-with-most-water/slides.pdf) · [PNGs](content/0011-container-with-most-water/slides/) | [Java](java/src/main/java/twopointers/ContainerWithMostWater.java) |
| 0015. 3Sum | Medium | [LeetCode](https://leetcode.com/problems/3sum/) | [Explanation](content/0015-3sum/explanation.md) | [Slides PDF](content/0015-3sum/slides.pdf) · [PNGs](content/0015-3sum/slides/) | [Java](java/src/main/java/twopointers/ThreeSum.java) |
| 0042. Trapping Rain Water | Hard | [LeetCode](https://leetcode.com/problems/trapping-rain-water/) | [Explanation](content/0042-trapping-rain-water/explanation.md) | [Slides PDF](content/0042-trapping-rain-water/slides.pdf) · [PNGs](content/0042-trapping-rain-water/slides/) | [Java](java/src/main/java/twopointers/TrappingRainWater.java) |
| 0125. Valid Palindrome | Easy | [LeetCode](https://leetcode.com/problems/valid-palindrome/) | [Explanation](content/0125-valid-palindrome/explanation.md) | [Slides PDF](content/0125-valid-palindrome/slides.pdf) · [PNGs](content/0125-valid-palindrome/slides/) | [Java](java/src/main/java/twopointers/ValidPalindrome.java) |
| 0167. Two Sum II - Input Array Is Sorted | Medium | [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Explanation](content/0167-two-sum-ii-input-array-is-sorted/explanation.md) | [Slides PDF](content/0167-two-sum-ii-input-array-is-sorted/slides.pdf) · [PNGs](content/0167-two-sum-ii-input-array-is-sorted/slides/) | [Java](java/src/main/java/twopointers/TwoSumII.java) |

## Sliding Window (6)

| Problem | Difficulty | Link | Explanation | Slides | Code |
|---|---|---|---|---|---|
| 0003. Longest Substring Without Repeating Characters | Medium | [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Explanation](content/0003-longest-substring-without-repeating-characters/explanation.md) | [Slides PDF](content/0003-longest-substring-without-repeating-characters/slides.pdf) · [PNGs](content/0003-longest-substring-without-repeating-characters/slides/) | [Java](java/src/main/java/slidingwindow/LongestSubstringWithoutRepeating.java) |
| 0076. Minimum Window Substring | Hard | [LeetCode](https://leetcode.com/problems/minimum-window-substring/) | [Explanation](content/0076-minimum-window-substring/explanation.md) | [Slides PDF](content/0076-minimum-window-substring/slides.pdf) · [PNGs](content/0076-minimum-window-substring/slides/) | [Java](java/src/main/java/slidingwindow/MinimumWindowSubstring.java) |
| 0121. Best Time to Buy and Sell Stock | Easy | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Explanation](content/0121-best-time-to-buy-and-sell-stock/explanation.md) | [Slides PDF](content/0121-best-time-to-buy-and-sell-stock/slides.pdf) · [PNGs](content/0121-best-time-to-buy-and-sell-stock/slides/) | [Java](java/src/main/java/slidingwindow/BestTimeToBuyAndSellStock.java) |
| 0239. Sliding Window Maximum | Hard | [LeetCode](https://leetcode.com/problems/sliding-window-maximum/) | [Explanation](content/0239-sliding-window-maximum/explanation.md) | [Slides PDF](content/0239-sliding-window-maximum/slides.pdf) · [PNGs](content/0239-sliding-window-maximum/slides/) | [Java](java/src/main/java/slidingwindow/SlidingWindowMaximum.java) |
| 0424. Longest Repeating Character Replacement | Medium | [LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/) | [Explanation](content/0424-longest-repeating-character-replacement/explanation.md) | [Slides PDF](content/0424-longest-repeating-character-replacement/slides.pdf) · [PNGs](content/0424-longest-repeating-character-replacement/slides/) | [Java](java/src/main/java/slidingwindow/LongestRepeatingCharacterReplacement.java) |
| 0567. Permutation in String | Medium | [LeetCode](https://leetcode.com/problems/permutation-in-string/) | [Explanation](content/0567-permutation-in-string/explanation.md) | [Slides PDF](content/0567-permutation-in-string/slides.pdf) · [PNGs](content/0567-permutation-in-string/slides/) | [Java](java/src/main/java/slidingwindow/PermutationInString.java) |

## Stack (7)

| Problem | Difficulty | Link | Explanation | Slides | Code |
|---|---|---|---|---|---|
| 0020. Valid Parentheses | Easy | [LeetCode](https://leetcode.com/problems/valid-parentheses/) | [Explanation](content/0020-valid-parentheses/explanation.md) | [Slides PDF](content/0020-valid-parentheses/slides.pdf) · [PNGs](content/0020-valid-parentheses/slides/) | [Java](java/src/main/java/stack/ValidParentheses.java) |
| 0022. Generate Parentheses | Medium | [LeetCode](https://leetcode.com/problems/generate-parentheses/) | [Explanation](content/0022-generate-parentheses/explanation.md) | [Slides PDF](content/0022-generate-parentheses/slides.pdf) · [PNGs](content/0022-generate-parentheses/slides/) | [Java](java/src/main/java/stack/GenerateParentheses.java) |
| 0084. Largest Rectangle in Histogram | Hard | [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Explanation](content/0084-largest-rectangle-in-histogram/explanation.md) | [Slides PDF](content/0084-largest-rectangle-in-histogram/slides.pdf) · [PNGs](content/0084-largest-rectangle-in-histogram/slides/) | [Java](java/src/main/java/stack/LargestRectangleInHistogram.java) |
| 0150. Evaluate Reverse Polish Notation | Medium | [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [Explanation](content/0150-evaluate-reverse-polish-notation/explanation.md) | [Slides PDF](content/0150-evaluate-reverse-polish-notation/slides.pdf) · [PNGs](content/0150-evaluate-reverse-polish-notation/slides/) | [Java](java/src/main/java/stack/EvaluateReversePolishNotation.java) |
| 0155. Min Stack | Medium | [LeetCode](https://leetcode.com/problems/min-stack/) | [Explanation](content/0155-min-stack/explanation.md) | [Slides PDF](content/0155-min-stack/slides.pdf) · [PNGs](content/0155-min-stack/slides/) | [Java](java/src/main/java/stack/MinStack.java) |
| 0739. Daily Temperatures | Medium | [LeetCode](https://leetcode.com/problems/daily-temperatures/) | [Explanation](content/0739-daily-temperatures/explanation.md) | [Slides PDF](content/0739-daily-temperatures/slides.pdf) · [PNGs](content/0739-daily-temperatures/slides/) | [Java](java/src/main/java/stack/DailyTemperatures.java) |
| 0853. Car Fleet | Medium | [LeetCode](https://leetcode.com/problems/car-fleet/) | [Explanation](content/0853-car-fleet/explanation.md) | [Slides PDF](content/0853-car-fleet/slides.pdf) · [PNGs](content/0853-car-fleet/slides/) | [Java](java/src/main/java/stack/CarFleet.java) |

## Binary Search (7)

| Problem | Difficulty | Link | Explanation | Slides | Code |
|---|---|---|---|---|---|
| 0004. Median of Two Sorted Arrays | Hard | [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [Explanation](content/0004-median-of-two-sorted-arrays/explanation.md) | [Slides PDF](content/0004-median-of-two-sorted-arrays/slides.pdf) · [PNGs](content/0004-median-of-two-sorted-arrays/slides/) | [Java](java/src/main/java/binarysearch/MedianOfTwoSortedArrays.java) |
| 0033. Search in Rotated Sorted Array | Medium | [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Explanation](content/0033-search-in-rotated-sorted-array/explanation.md) | [Slides PDF](content/0033-search-in-rotated-sorted-array/slides.pdf) · [PNGs](content/0033-search-in-rotated-sorted-array/slides/) | [Java](java/src/main/java/binarysearch/SearchInRotatedSortedArray.java) |
| 0074. Search a 2D Matrix | Medium | [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/) | [Explanation](content/0074-search-a-2d-matrix/explanation.md) | [Slides PDF](content/0074-search-a-2d-matrix/slides.pdf) · [PNGs](content/0074-search-a-2d-matrix/slides/) | [Java](java/src/main/java/binarysearch/SearchA2DMatrix.java) |
| 0153. Find Minimum in Rotated Sorted Array | Medium | [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Explanation](content/0153-find-minimum-in-rotated-sorted-array/explanation.md) | [Slides PDF](content/0153-find-minimum-in-rotated-sorted-array/slides.pdf) · [PNGs](content/0153-find-minimum-in-rotated-sorted-array/slides/) | [Java](java/src/main/java/binarysearch/FindMinimumInRotatedSortedArray.java) |
| 0704. Binary Search | Easy | [LeetCode](https://leetcode.com/problems/binary-search/) | [Explanation](content/0704-binary-search/explanation.md) | [Slides PDF](content/0704-binary-search/slides.pdf) · [PNGs](content/0704-binary-search/slides/) | [Java](java/src/main/java/binarysearch/BinarySearch.java) |
| 0875. Koko Eating Bananas | Medium | [LeetCode](https://leetcode.com/problems/koko-eating-bananas/) | [Explanation](content/0875-koko-eating-bananas/explanation.md) | [Slides PDF](content/0875-koko-eating-bananas/slides.pdf) · [PNGs](content/0875-koko-eating-bananas/slides/) | [Java](java/src/main/java/binarysearch/KokoEatingBananas.java) |
| 0981. Time Based Key-Value Store | Medium | [LeetCode](https://leetcode.com/problems/time-based-key-value-store/) | [Explanation](content/0981-time-based-key-value-store/explanation.md) | [Slides PDF](content/0981-time-based-key-value-store/slides.pdf) · [PNGs](content/0981-time-based-key-value-store/slides/) | [Java](java/src/main/java/binarysearch/TimeMap.java) |
