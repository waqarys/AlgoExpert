package dp1;

/**
 * LC 198 House Robber.
 * Approach: dp[i] = max(dp[i-1], dp[i-2] + nums[i]) with two variables.
 * Time O(n), Space O(1).
 */
public class HouseRobber {
    public int rob(int[] nums) { return rob(nums, 0, nums.length - 1); }

    /** Rob houses in the inclusive range [lo, hi]; reused by House Robber II. */
    public int rob(int[] nums, int lo, int hi) {
        int prev2 = 0, prev1 = 0;
        for (int i = lo; i <= hi; i++) {
            int cur = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
