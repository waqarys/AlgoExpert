package graphs;

import java.util.*;

/**
 * LC 417 Pacific Atlantic Water Flow.
 * Approach: reverse DFS uphill from each ocean's border; answer = cells reached by both.
 * Time O(mn), Space O(mn).
 */
public class PacificAtlanticWaterFlow {
    public List<List<Integer>> pacificAtlantic(int[][] h) {
        int m = h.length, n = h[0].length;
        boolean[][] pac = new boolean[m][n], atl = new boolean[m][n];
        for (int r = 0; r < m; r++) { dfs(h, r, 0, pac, h[r][0]); dfs(h, r, n - 1, atl, h[r][n - 1]); }
        for (int c = 0; c < n; c++) { dfs(h, 0, c, pac, h[0][c]); dfs(h, m - 1, c, atl, h[m - 1][c]); }
        List<List<Integer>> res = new ArrayList<>();
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) if (pac[r][c] && atl[r][c]) res.add(List.of(r, c));
        return res;
    }

    private void dfs(int[][] h, int r, int c, boolean[][] seen, int prev) {
        if (r < 0 || c < 0 || r >= h.length || c >= h[0].length || seen[r][c] || h[r][c] < prev) return;
        seen[r][c] = true;
        dfs(h, r + 1, c, seen, h[r][c]); dfs(h, r - 1, c, seen, h[r][c]);
        dfs(h, r, c + 1, seen, h[r][c]); dfs(h, r, c - 1, seen, h[r][c]);
    }
}
