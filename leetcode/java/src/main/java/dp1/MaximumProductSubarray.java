package dp1;

/**
 * LC 152 Maximum Product Subarray.
 * Approach: track max and min product ending here (negatives swap them).
 * Time O(n), Space O(1).
 */
public class MaximumProductSubarray {
    public int maxProduct(int[] nums) {
        int hi = nums[0], lo = nums[0], best = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int x = nums[i], a = hi * x, b = lo * x;
            hi = Math.max(x, Math.max(a, b));
            lo = Math.min(x, Math.min(a, b));
            best = Math.max(best, hi);
        }
        return best;
    }
}
