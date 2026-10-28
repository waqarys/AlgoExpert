package medium.dynamicprogramming;

/**
 * Number Of Ways To Traverse Graph: paths from top-left to bottom-right of a width x height grid moving
 * only right/down. Equals C(w+h-2, w-1), computed incrementally to avoid overflow.
 * Time: O(min(w, h)) | Space: O(1).
 */
public class NumberOfWaysToTraverseGraph {
    public static long numberOfWaysToTraverseGraph(int width, int height) {
        int n = width + height - 2, k = Math.min(width, height) - 1;
        long r = 1;
        for (int i = 1; i <= k; i++) r = r * (n - k + i) / i;
        return r;
    }
}
