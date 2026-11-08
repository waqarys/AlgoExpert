# 0046. Permutations

**Difficulty:** Medium | **Category:** Backtracking | **LeetCode:** https://leetcode.com/problems/permutations/

## Problem
- Return all permutations of an array of distinct integers.

## Intuition
- Build the permutation position by position; at each step choose any unused element.
- A boolean used[] array tracks what is already in the path.

## Brute Force
- Generate all n^n sequences and filter those with distinct elements.

## Optimal Approach
1. If path.size() == n, record.
2. For each i not used: mark, add, recurse, unmark, remove.

## Worked Example
- [1,2,3].
```text
1 -> 2 -> 3   [1,2,3]
  -> 3 -> 2   [1,3,2]
2 -> 1 -> 3 ; 2 -> 3 -> 1
3 -> 1 -> 2 ; 3 -> 2 -> 1
6 permutations
```

## Complexity
- Time: O(n * n!). Space: O(n).

## Pitfalls
- Permutations iterate from 0 each time (order matters); subsets/combinations iterate from start.

## Video Script
- Side by side: subsets tree vs permutations tree.

## Solution
```java file=backtracking/Permutations.java
package backtracking;

import java.util.*;

/**
 * LC 46 Permutations.
 * Approach: backtracking with a used[] array.
 * Time O(n * n!), Space O(n).
 */
public class Permutations {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(nums, new boolean[nums.length], new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] nums, boolean[] used, List<Integer> path, List<List<Integer>> res) {
        if (path.size() == nums.length) { res.add(new ArrayList<>(path)); return; }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            used[i] = true;
            path.add(nums[i]);
            dfs(nums, used, path, res);
            path.remove(path.size() - 1);
            used[i] = false;
        }
    }
}
```

## Tests
```java test=backtracking/PermutationsTest.java
package backtracking;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class PermutationsTest {
    @Test void examples() {
        assertEquals(List.of(List.of(1, 2, 3), List.of(1, 3, 2), List.of(2, 1, 3), List.of(2, 3, 1), List.of(3, 1, 2), List.of(3, 2, 1)),
                new Permutations().permute(new int[]{1, 2, 3}));
        assertEquals(List.of(List.of(1)), new Permutations().permute(new int[]{1}));
        assertEquals(24, new Permutations().permute(new int[]{1, 2, 3, 4}).size());
    }
}
```
