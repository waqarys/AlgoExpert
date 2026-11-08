---
title: Two Sum
subtitle: One pass with a HashMap of value → index
series: LeetCode · NeetCode 150 · #0001
lower_topic: LeetCode 1 · Two Sum · Arrays & Hashing
next: Next up · LeetCode 36 · Valid Sudoku
repo: github.com/waqarys/AlgoExpert/tree/leetcode/leetcode
thumb_big: TWO SUM
thumb_small: Return indices in O(n)
thumb_tag: LEETCODE #1
source: leetcode/java/src/main/java/arrays/TwoSum.java
---
# Hook
[face] LeetCode problem number one, and the twist that trips people up: it asks for indices, not values. Let's nail it the way interviewers expect.

# Problem
[02] Given an integer array nums and a target, return the indices of the two numbers that add up to the target. There is exactly one valid answer, and you may not use the same element twice.

# Examples & Constraints
[06] For example, nums three, two, four with target six returns indices one and two. Note that three plus three is not allowed, because that would reuse index zero. Because we need indices, sorting the array is off the table.

# Brute Force
[04] The brute force tries every pair i less than j, and checks whether nums i plus nums j equals the target. That's O of n squared time and O of one space. {key: Brute force O(n²) time · O(1) space}

# Optimized Approach
[03] The insight: for each x, the partner we need is target minus x. If we remember every value we've passed, mapped to its index, we can find the partner in constant time.
[05] So keep a HashMap from value to index. For each index i, if the map contains the complement, return the stored index and i. Otherwise store nums i and continue. {key: Map value → index · check before you insert}

# Dry Run
[06] Trace three, two, four with target six. Index zero: need three, map is empty, store three at zero. Index one: need four, missing, store two at one. Index two: need two, found at index one. Return one, two.

# Java Walkthrough
[face-pip 07] In Java, the map is a HashMap of Integer to Integer. Inside the loop we look up target minus nums i. If it's not null, we return the pair of indices. Below it, I kept the brute force version for comparison.

# Complexity
[08] One pass over the array gives O of n time, and the map uses O of n extra space. {key: O(n) time · O(n) space}

# Edge Cases & Recap
[09] Two pitfalls: return indices, not values, and don't sort, because it destroys the original indices. The solution and tests are on the leetcode branch of the AlgoExpert repo. I'm Waqar, see you in the next problem.
