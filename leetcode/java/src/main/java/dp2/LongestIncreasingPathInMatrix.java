package dp2;

/**
 * LC 329 Longest Increasing Path in a Matrix.
 * Approach: DFS with memoization over the implicit DAG of increasing moves.
 * Time O(mn), Space O(mn).
 */
public class LongestIncreasingPathInMatrix {
    private static final int[][] DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int longestIncreasingPath(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length, best = 0;
        int[][] memo = new int[m][n];
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) best = Math.max(best, dfs(matrix, r, c, memo));
        return best;
    }

    private int dfs(int[][] g, int r, int c, int[][] memo) {
        if (memo[r][c] != 0) return memo[r][c];
        int best = 1;
        for (int[] d : DIRS) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nc >= 0 && nr < g.length && nc < g[0].length && g[nr][nc] > g[r][c])
                best = Math.max(best, 1 + dfs(g, nr, nc, memo));
        }
        return memo[r][c] = best;
    }
}
