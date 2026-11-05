package dp1;

/**
 * LC 416 Partition Equal Subset Sum.
 * Approach: 0/1 knapsack boolean DP for total/2, iterating sums downward.
 * Time O(n * sum), Space O(sum).
 */
public class PartitionEqualSubsetSum {
    public boolean canPartition(int[] nums) {
        int total = 0;
        for (int x : nums) total += x;
        if (total % 2 == 1) return false;
        int target = total / 2;
        boolean[] can = new boolean[target + 1];
        can[0] = true;
        for (int x : nums)
            for (int s = target; s >= x; s--) can[s] |= can[s - x];
        return can[target];
    }
}
