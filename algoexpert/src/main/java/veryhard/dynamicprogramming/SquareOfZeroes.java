package veryhard.dynamicprogramming;

/**
 * Square Of Zeroes: does the 0/1 matrix contain a square (side >= 2) whose border is entirely 0s?
 * Precompute consecutive zeros to the right and downward per cell.
 * Time: O(n^3) | Space: O(n^2).
 */
public class SquareOfZeroes {
    public static boolean squareOfZeroes(int[][] m) {
        int n = m.length;
        int[][] right = new int[n + 1][n + 1], down = new int[n + 1][n + 1];
        for (int r = n - 1; r >= 0; r--) for (int c = n - 1; c >= 0; c--) if (m[r][c] == 0) {
            right[r][c] = right[r][c + 1] + 1;
            down[r][c] = down[r + 1][c] + 1;
        }
        for (int r = 0; r < n; r++) for (int c = 0; c < n; c++)
            for (int s = 2; r + s <= n && c + s <= n; s++)
                if (right[r][c] >= s && down[r][c] >= s && right[r + s - 1][c] >= s && down[r][c + s - 1] >= s) return true;
        return false;
    }
}
