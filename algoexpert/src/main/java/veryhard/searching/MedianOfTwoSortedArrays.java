package veryhard.searching;

/**
 * Median Of Two Sorted Arrays: median of the union of two sorted arrays via binary-searched partition.
 * Time: O(log(min(n, m))) | Space: O(1).
 */
public class MedianOfTwoSortedArrays {
    public static float medianOfTwoSortedArrays(int[] a, int[] b) {
        if (a.length > b.length) return medianOfTwoSortedArrays(b, a);
        int n = a.length, m = b.length, half = (n + m + 1) / 2, lo = 0, hi = n;
        while (true) {
            int i = (lo + hi) / 2, j = half - i;
            int aL = i == 0 ? Integer.MIN_VALUE : a[i - 1], aR = i == n ? Integer.MAX_VALUE : a[i];
            int bL = j == 0 ? Integer.MIN_VALUE : b[j - 1], bR = j == m ? Integer.MAX_VALUE : b[j];
            if (aL > bR) hi = i - 1;
            else if (bL > aR) lo = i + 1;
            else {
                if ((n + m) % 2 == 1) return Math.max(aL, bL);
                return (Math.max(aL, bL) + (float) Math.min(aR, bR)) / 2;
            }
        }
    }
}
