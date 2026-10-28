package hard.dynamicprogramming;

/**
 * Maximum Sum Submatrix: largest sum among all size x size square submatrices, using 2D prefix sums.
 * Time: O(w*h) | Space: O(w*h).
 */
public class MaximumSumSubmatrix {
    public static int maximumSumSubmatrix(int[][] m, int size) {
        int R = m.length, C = m[0].length;
        int[][] p = new int[R + 1][C + 1];
        for (int r = 0; r < R; r++) for (int c = 0; c < C; c++) p[r + 1][c + 1] = m[r][c] + p[r][c + 1] + p[r + 1][c] - p[r][c];
        int best = Integer.MIN_VALUE;
        for (int r = size; r <= R; r++) for (int c = size; c <= C; c++)
            best = Math.max(best, p[r][c] - p[r - size][c] - p[r][c - size] + p[r - size][c - size]);
        return best;
    }
}
