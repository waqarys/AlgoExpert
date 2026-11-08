package arrays;

import java.util.*;

/**
 * LC 217 Contains Duplicate. Return true if any value repeats.
 * Approach: single pass with a HashSet; add() returns false on a repeat.
 * Time O(n), Space O(n).
 */
public class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int x : nums) {
            if (!seen.add(x)) return true;
        }
        return false;
    }

    /** Teaching baseline: sort and compare neighbours. O(n log n) time. */
    public boolean containsDuplicateSort(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        for (int i = 1; i < a.length; i++) if (a[i] == a[i - 1]) return true;
        return false;
    }
}
