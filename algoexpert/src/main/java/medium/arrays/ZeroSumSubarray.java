package medium.arrays;

import java.util.HashSet;
import java.util.Set;

/**
 * Zero Sum Subarray: does any non-empty contiguous subarray sum to zero? A repeated prefix sum proves it.
 * Time: O(n) | Space: O(n).
 */
public class ZeroSumSubarray {
    public static boolean zeroSumSubarray(int[] nums) {
        Set<Long> seen = new HashSet<>();
        seen.add(0L);
        long sum = 0;
        for (int n : nums) { sum += n; if (!seen.add(sum)) return true; }
        return false;
    }
}
