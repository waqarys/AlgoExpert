package math;

/**
 * LC 48 Rotate Image.
 * Approach: transpose then reverse each row.
 * Time O(n^2), Space O(1).
 */
public class RotateImage {
    public void rotate(int[][] m) {
        int n = m.length;
        for (int r = 0; r < n; r++)
            for (int c = r + 1; c < n; c++) { int t = m[r][c]; m[r][c] = m[c][r]; m[c][r] = t; }
        for (int[] row : m)
            for (int l = 0, r = n - 1; l < r; l++, r--) { int t = row[l]; row[l] = row[r]; row[r] = t; }
    }
}
