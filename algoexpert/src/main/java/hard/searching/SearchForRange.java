package hard.searching;

/**
 * Search For Range: first and last index of target in a sorted array, [-1, -1] if absent.
 * Two modified binary searches.
 * Time: O(log n) | Space: O(1).
 */
public class SearchForRange {
    public static int[] searchForRange(int[] a, int t) {
        int l = bound(a, t), r = bound(a, t + 1) - 1;
        return l <= r && l < a.length && a[l] == t ? new int[]{l, r} : new int[]{-1, -1};
    }

    private static int bound(int[] a, int t) {
        int lo = 0, hi = a.length;
        while (lo < hi) { int m = (lo + hi) >>> 1; if (a[m] < t) lo = m + 1; else hi = m; }
        return lo;
    }
}
