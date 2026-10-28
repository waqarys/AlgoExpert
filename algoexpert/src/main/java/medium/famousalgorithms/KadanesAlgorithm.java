package medium.famousalgorithms;

/**
 * Kadane's Algorithm: maximum sum of a non-empty contiguous subarray.
 * Time: O(n) | Space: O(1).
 */
public class KadanesAlgorithm {
    public static int kadanesAlgorithm(int[] a) {
        int cur = a[0], best = a[0];
        for (int i = 1; i < a.length; i++) { cur = Math.max(a[i], cur + a[i]); best = Math.max(best, cur); }
        return best;
    }
}
