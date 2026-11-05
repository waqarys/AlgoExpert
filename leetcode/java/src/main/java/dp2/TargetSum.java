package dp2;

/**
 * LC 494 Target Sum.
 * Approach: reduce to counting subsets with sum (total + target) / 2 (0/1 knapsack).
 * Time O(n * sum), Space O(sum).
 */
public class TargetSum {
    public int findTargetSumWays(int[] nums, int target) {
        int total = 0;
        for (int x : nums) total += x;
        if (Math.abs(target) > total || (total + target) % 2 != 0) return 0;
        int s = (total + target) / 2;
        int[] ways = new int[s + 1];
        ways[0] = 1;
        for (int x : nums)
            for (int t = s; t >= x; t--) ways[t] += ways[t - x];
        return ways[s];
    }
}
