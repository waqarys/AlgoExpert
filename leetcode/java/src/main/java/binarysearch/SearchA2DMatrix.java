package binarysearch;

/**
 * LC 74 Search a 2D Matrix.
 * Approach: binary search over the virtual flattened array, index k -> (k / n, k % n).
 * Time O(log(mn)), Space O(1).
 */
public class SearchA2DMatrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length, lo = 0, hi = m * n - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2, v = matrix[mid / n][mid % n];
            if (v == target) return true;
            if (v < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return false;
    }
}
