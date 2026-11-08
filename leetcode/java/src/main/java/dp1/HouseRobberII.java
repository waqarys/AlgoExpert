package dp1;

/**
 * LC 213 House Robber II.
 * Approach: circle -> max of two linear robberies excluding first or last house.
 * Time O(n), Space O(1).
 */
public class HouseRobberII {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        HouseRobber linear = new HouseRobber();
        return Math.max(linear.rob(nums, 0, n - 2), linear.rob(nums, 1, n - 1));
    }
}
