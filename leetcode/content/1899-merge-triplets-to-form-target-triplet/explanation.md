# 1899. Merge Triplets to Form Target Triplet

**Difficulty:** Medium | **Category:** Greedy | **LeetCode:** https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

## Problem
- Merging two triplets takes the element-wise max. Can some sequence of merges produce exactly target?

## Intuition
- A triplet with any value greater than target in some position would overshoot forever, so ignore it.
- Among the safe triplets, each target coordinate just needs to be matched exactly by at least one of them.

## Brute Force
- Try all subsets of triplets: O(2^n).

## Optimal Approach
1. found[3] = false.
2. For each triplet t with t[k] <= target[k] for all k: for each k, if t[k] == target[k], found[k] = true.
3. Return true only if all three are found.

## Worked Example
- triplets [[2,5,3],[1,8,4],[1,7,5]], target [2,7,5].
```text
[2,5,3] safe -> matches x (2)
[1,8,4] 8 > 7 -> skip
[1,7,5] safe -> matches y (7) and z (5)
all matched -> true
```

## Complexity
- Time: O(n). Space: O(1).

## Pitfalls
- A single safe triplet can satisfy several coordinates.

## Video Script
- A short "filter, then cover" greedy.

## Solution
```java file=greedy/MergeTripletsToFormTarget.java
package greedy;

/**
 * LC 1899 Merge Triplets to Form Target Triplet.
 * Approach: discard triplets exceeding target anywhere; check each coordinate is hit exactly.
 * Time O(n), Space O(1).
 */
public class MergeTripletsToFormTarget {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        boolean[] found = new boolean[3];
        for (int[] t : triplets) {
            if (t[0] > target[0] || t[1] > target[1] || t[2] > target[2]) continue;
            for (int k = 0; k < 3; k++) if (t[k] == target[k]) found[k] = true;
        }
        return found[0] && found[1] && found[2];
    }
}
```

## Tests
```java test=greedy/MergeTripletsToFormTargetTest.java
package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MergeTripletsToFormTargetTest {
    MergeTripletsToFormTarget s = new MergeTripletsToFormTarget();
    @Test void examples() {
        assertTrue(s.mergeTriplets(new int[][]{{2, 5, 3}, {1, 8, 4}, {1, 7, 5}}, new int[]{2, 7, 5}));
        assertFalse(s.mergeTriplets(new int[][]{{3, 4, 5}, {4, 5, 6}}, new int[]{3, 2, 5}));
        assertTrue(s.mergeTriplets(new int[][]{{2, 5, 3}, {2, 3, 4}, {1, 2, 5}, {5, 2, 3}}, new int[]{5, 5, 5}));
    }
}
```
