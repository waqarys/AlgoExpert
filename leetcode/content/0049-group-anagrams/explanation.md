# 0049. Group Anagrams

**Difficulty:** Medium | **Category:** Arrays & Hashing | **LeetCode:** https://leetcode.com/problems/group-anagrams/

## Problem
- Given an array of strings, group the anagrams together. Any order of groups is accepted.
- Example: ["eat","tea","tan","ate","nat","bat"] -> [["bat"],["nat","tan"],["ate","eat","tea"]].

## Intuition
- All anagrams share a canonical "signature". If we compute it, a HashMap from signature to list does the grouping.
- Signature options: the sorted word (O(k log k)) or a 26-letter count encoding (O(k)).

## Brute Force
- Compare every word with every existing group using an anagram check: O(n^2 * k).

## Optimal Approach
1. For each word, build a count array of 26 letters.
2. Encode the counts as a key like "#1#0#0...#1" (separators avoid ambiguity such as 1,11 vs 11,1).
3. computeIfAbsent(key, new list).add(word).
4. Return the map's values.

## Worked Example
- words = ["eat","tea","tan","ate","nat","bat"], key shown as letters that occur.
```text
eat -> a1 e1 t1  -> group A [eat]
tea -> a1 e1 t1  -> group A [eat,tea]
tan -> a1 n1 t1  -> group B [tan]
ate -> a1 e1 t1  -> group A [eat,tea,ate]
nat -> a1 n1 t1  -> group B [tan,nat]
bat -> a1 b1 t1  -> group C [bat]
```

## Complexity
- Time: O(n * k) where k is the max word length.
- Space: O(n * k) for keys and groups.

## Pitfalls
- Using a count key without separators can collide.
- int[] cannot be a HashMap key directly (identity hashing); convert it to a String or a List.

## Video Script
- Recall Valid Anagram, then ask: how do we bucket instead of compare?
- Show the sorted-key solution first, then the counting key as the upgrade.
- Trace the example and point out the map is doing all the grouping work.

## Solution
```java file=arrays/GroupAnagrams.java
package arrays;

import java.util.*;

/**
 * LC 49 Group Anagrams.
 * Approach: canonical key = encoded 26-letter counts; bucket words in a HashMap.
 * Time O(n*k), Space O(n*k).
 */
public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();
        for (String w : strs) {
            int[] count = new int[26];
            for (char c : w.toCharArray()) count[c - 'a']++;
            StringBuilder key = new StringBuilder();
            for (int c : count) key.append('#').append(c);
            groups.computeIfAbsent(key.toString(), k -> new ArrayList<>()).add(w);
        }
        return new ArrayList<>(groups.values());
    }
}
```

## Tests
```java test=arrays/GroupAnagramsTest.java
package arrays;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class GroupAnagramsTest {
    static Set<Set<String>> norm(List<List<String>> g) {
        Set<Set<String>> out = new HashSet<>();
        for (List<String> l : g) out.add(new HashSet<>(l));
        return out;
    }
    @Test void example() {
        var r = new GroupAnagrams().groupAnagrams(new String[]{"eat", "tea", "tan", "ate", "nat", "bat"});
        assertEquals(Set.of(Set.of("bat"), Set.of("nat", "tan"), Set.of("ate", "eat", "tea")), norm(r));
    }
    @Test void edges() {
        assertEquals(List.of(List.of("")), new GroupAnagrams().groupAnagrams(new String[]{""}));
        assertEquals(List.of(List.of("a")), new GroupAnagrams().groupAnagrams(new String[]{"a"}));
    }
}
```
