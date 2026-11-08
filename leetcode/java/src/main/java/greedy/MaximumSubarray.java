package greedy;

/**
 * LC 53 Maximum Subarray.
 * Approach: Kadane - extend the running sum or restart at x.
 * Time O(n), Space O(1).
 */
public class MaximumSubarray {
    public int maxSubArray(int[] nums) {
        int cur = 0, best = Integer.MIN_VALUE;
        for (int x : nums) {
            cur = Math.max(x, cur + x);
            best = Math.max(best, cur);
        }
        return best;
    }
}
