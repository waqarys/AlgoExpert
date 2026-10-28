package medium.searching;

/**
 * Search In Sorted Matrix: rows and columns are sorted ascending; return [row, col] of target or [-1, -1].
 * Start top-right and eliminate a row or column each step.
 * Time: O(n + m) | Space: O(1).
 */
public class SearchInSortedMatrix {
    public static int[] searchInSortedMatrix(int[][] m, int target) {
        int r = 0, c = m[0].length - 1;
        while (r < m.length && c >= 0) {
            if (m[r][c] == target) return new int[]{r, c};
            if (m[r][c] > target) c--; else r++;
        }
        return new int[]{-1, -1};
    }
}
