package dp1;

/**
 * LC 300 Longest Increasing Subsequence.
 * Approach: patience sorting; tails[k] = smallest tail of an increasing subsequence of length k+1.
 * Time O(n log n), Space O(n).
 */
public class LongestIncreasingSubsequence {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for (int x : nums) {
            int lo = 0, hi = size;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (tails[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            tails[lo] = x;
            if (lo == size) size++;
        }
        return size;
    }

    /** O(n^2) DP for teaching. */
    public int lengthOfLISQuadratic(int[] nums) {
        int[] dp = new int[nums.length];
        int best = 0;
        for (int i = 0; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
            best = Math.max(best, dp[i]);
        }
        return best;
    }
}
