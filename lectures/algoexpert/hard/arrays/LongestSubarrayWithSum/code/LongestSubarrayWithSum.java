public class LongestSubarrayWithSum {
    public static int[] longestSubarrayWithSum(int[] a, int target) {
        int[] best = {};
        int l = 0, sum = 0;
        for (int r = 0; r < a.length; r++) {
            sum += a[r];
            while (sum > target && l < r) sum -= a[l++];
            if (sum == target && (best.length == 0 || r - l > best[1] - best[0])) best = new int[]{l, r};
        }
        return best;
    }
}
