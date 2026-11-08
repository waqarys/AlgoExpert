# 0763. Partition Labels

**Difficulty:** Medium | **Category:** Greedy | **LeetCode:** https://leetcode.com/problems/partition-labels/

## Problem
- Split s into as many parts as possible so each letter appears in at most one part. Return the part sizes.

## Intuition
- Record each letter's last index. While scanning, the current part must extend at least to the last occurrence of every letter seen in it.
- When i reaches that end, the part can be closed.

## Brute Force
- Try all cut positions and validate: O(n^2) or worse.

## Optimal Approach
1. last[c] = last index of c.
2. start = 0, end = 0. For i: end = max(end, last[s[i]]); if i == end: record end - start + 1; start = i + 1.

## Worked Example
- "ababcbacadefegdehijhklij".
```text
part 1: a..a ends at 8   -> "ababcbaca" (9)
part 2: d..e ends at 15  -> "defegde"   (7)
part 3: h..j ends at 23  -> "hijhklij"  (8)
```

## Complexity
- Time: O(n). Space: O(26).

## Pitfalls
- end only grows within a part.

## Video Script
- Interval merging in disguise: each letter is the interval [first, last].

## Solution
```java file=greedy/PartitionLabels.java
package greedy;

import java.util.*;

/**
 * LC 763 Partition Labels.
 * Approach: last-occurrence table; close a part when i reaches the furthest last index seen.
 * Time O(n), Space O(1).
 */
public class PartitionLabels {
    public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        for (int i = 0; i < s.length(); i++) last[s.charAt(i) - 'a'] = i;
        List<Integer> res = new ArrayList<>();
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            end = Math.max(end, last[s.charAt(i) - 'a']);
            if (i == end) { res.add(end - start + 1); start = i + 1; }
        }
        return res;
    }
}
```

## Tests
```java test=greedy/PartitionLabelsTest.java
package greedy;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class PartitionLabelsTest {
    PartitionLabels s = new PartitionLabels();
    @Test void examples() {
        assertEquals(List.of(9, 7, 8), s.partitionLabels("ababcbacadefegdehijhklij"));
        assertEquals(List.of(10), s.partitionLabels("eccbbbbdec"));
        assertEquals(List.of(1, 1, 1), s.partitionLabels("abc"));
    }
}
```
