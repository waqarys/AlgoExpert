package arrays;

import java.util.*;

/**
 * LC 1 Two Sum. Indices of two numbers summing to target.
 * Approach: one-pass HashMap of value -> index; look up the complement before inserting.
 * Time O(n), Space O(n).
 */
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> index = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer j = index.get(target - nums[i]);
            if (j != null) return new int[]{j, i};
            index.put(nums[i], i);
        }
        return new int[0];
    }

    /** Brute force for comparison. O(n^2). */
    public int[] twoSumBrute(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++)
            for (int j = i + 1; j < nums.length; j++)
                if (nums[i] + nums[j] == target) return new int[]{i, j};
        return new int[0];
    }
}
