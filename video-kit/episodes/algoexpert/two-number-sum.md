---
title: Two Number Sum
subtitle: From O(n²) to one pass with a HashSet
series: AlgoExpert · Easy · Arrays
lower_topic: Two Number Sum · AlgoExpert Easy
next: Next up · AlgoExpert · Validate Subsequence
repo: github.com/waqarys/AlgoExpert (leetcode branch)
thumb_big: TWO NUMBER SUM
thumb_small: O(n²) → O(n)
thumb_tag: ALGOEXPERT
source: algoexpert/src/main/java/easy/arrays/TwoNumberSum.java
---
# Hook
[face] Two numbers, one target, and an interviewer watching your complexity. Let's go from n squared to a single pass in under three minutes.

# Problem
[02] We get an array of distinct integers and a target sum. If any two numbers add up to the target, return them as a pair. If no pair exists, return an empty array.

# Examples & Constraints
[06] Our running example is three, five, minus four, eight, eleven, one, minus one, six, with a target of ten. The integers are distinct, negatives are allowed, and a number cannot pair with itself.

# Brute Force
[04] The brute force checks every pair, which is n squared time. Sorting plus two pointers gets n log n with constant extra space. But we can do better on time. {key: Brute force O(n²) · sort + two pointers O(n log n)}

# Optimized Approach
[03] Here is the insight. For each number x, its partner is target minus x. A hash set of the values we have already seen answers "have I met the partner?" in constant time.
[05] So we walk the array once. Check whether target minus x is in the set. If it is, return the pair. Otherwise, add x and keep going. {key: Check the set first, then add x}

# Dry Run
[07] At three we need seven. Not seen yet, so we remember three.
[09] Five, minus four, and eight all miss their partners, so the set grows to three, five, minus four, eight.
[11] At eleven we need minus one, not there yet. One goes in too. Then at minus one we need eleven, and eleven is in the set. We return eleven and minus one.

# Java Walkthrough
[face-pip 12] In Java: create a HashSet of integers, loop over the array, and if the set contains target minus x, return a new array of target minus x and x. Otherwise add x. Falling out of the loop returns an empty array.

# Complexity
[13] We touch each number once, so time is O of n. The set can hold up to n values, so space is O of n. {key: O(n) time · O(n) space}

# Edge Cases & Recap
[14] Edge cases: no pair means an empty array, checking before adding means a number never pairs with itself, and negatives work exactly the same way.
[16] Recap: for each number, ask whether its partner has already appeared. The code is in the AlgoExpert repo, linked below. I'm Waqar, see you in the next one.
