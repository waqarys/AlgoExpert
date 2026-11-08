package binarysearch;

/**
 * LC 4 Median of Two Sorted Arrays.
 * Approach: binary search the partition of the shorter array so that both left halves <= both right halves.
 * Time O(log min(m,n)), Space O(1).
 */
public class MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] a, int[] b) {
        if (a.length > b.length) return findMedianSortedArrays(b, a);
        int m = a.length, n = b.length, half = (m + n + 1) / 2, lo = 0, hi = m;
        while (lo <= hi) {
            int i = (lo + hi) / 2, j = half - i;
            int aL = i > 0 ? a[i - 1] : Integer.MIN_VALUE, aR = i < m ? a[i] : Integer.MAX_VALUE;
            int bL = j > 0 ? b[j - 1] : Integer.MIN_VALUE, bR = j < n ? b[j] : Integer.MAX_VALUE;
            if (aL > bR) hi = i - 1;
            else if (bL > aR) lo = i + 1;
            else {
                if ((m + n) % 2 == 1) return Math.max(aL, bL);
                return (Math.max(aL, bL) + (double) Math.min(aR, bR)) / 2.0;
            }
        }
        throw new IllegalArgumentException("inputs not sorted");
    }
}
