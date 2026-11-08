package graphs;

/**
 * LC 130 Surrounded Regions.
 * Approach: mark border-connected 'O' as safe via DFS, then capture the rest.
 * Time O(mn), Space O(mn).
 */
public class SurroundedRegions {
    public void solve(char[][] b) {
        int m = b.length, n = b[0].length;
        for (int r = 0; r < m; r++) { mark(b, r, 0); mark(b, r, n - 1); }
        for (int c = 0; c < n; c++) { mark(b, 0, c); mark(b, m - 1, c); }
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) b[r][c] = b[r][c] == 'S' ? 'O' : 'X';
    }

    private void mark(char[][] b, int r, int c) {
        if (r < 0 || c < 0 || r >= b.length || c >= b[0].length || b[r][c] != 'O') return;
        b[r][c] = 'S';
        mark(b, r + 1, c); mark(b, r - 1, c); mark(b, r, c + 1); mark(b, r, c - 1);
    }
}
