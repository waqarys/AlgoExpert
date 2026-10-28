package hard.arrays;

/**
 * Min Rewards: each student gets >= 1 reward; a student scoring higher than an adjacent one gets more.
 * Minimum total. Two passes (left-to-right, right-to-left).
 * Time: O(n) | Space: O(n).
 */
public class MinRewards {
    public static int minRewards(int[] scores) {
        int n = scores.length;
        int[] r = new int[n];
        java.util.Arrays.fill(r, 1);
        for (int i = 1; i < n; i++) if (scores[i] > scores[i - 1]) r[i] = r[i - 1] + 1;
        for (int i = n - 2; i >= 0; i--) if (scores[i] > scores[i + 1]) r[i] = Math.max(r[i], r[i + 1] + 1);
        int sum = 0;
        for (int x : r) sum += x;
        return sum;
    }
}
