package twopointers;

/**
 * LC 167 Two Sum II (sorted input).
 * Approach: converging two pointers; move l up if the sum is small, r down if large.
 * Time O(n), Space O(1).
 */
public class TwoSumII {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;
        while (l < r) {
            int sum = numbers[l] + numbers[r];
            if (sum == target) return new int[]{l + 1, r + 1};
            if (sum < target) l++;
            else r--;
        }
        return new int[0];
    }
}
