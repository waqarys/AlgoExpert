package hard.searching;

/**
 * Index Equals Value: sorted distinct ints; smallest index i with a[i] == i, or -1. Binary search.
 * Time: O(log n) | Space: O(1).
 */
public class IndexEqualsValue {
    public static int indexEqualsValue(int[] a) {
        int lo = 0, hi = a.length - 1, ans = -1;
        while (lo <= hi) {
            int m = (lo + hi) >>> 1;
            if (a[m] < m) lo = m + 1;
            else { if (a[m] == m) ans = m; hi = m - 1; }
        }
        return ans;
    }
}
