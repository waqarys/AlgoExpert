package backtracking;

import java.util.*;

/**
 * LC 51 N-Queens.
 * Approach: row-by-row backtracking with column and two diagonal occupancy arrays.
 * Time O(n!), Space O(n^2).
 */
public class NQueens {
    public List<List<String>> solveNQueens(int n) {
        char[][] board = new char[n][n];
        for (char[] row : board) Arrays.fill(row, '.');
        List<List<String>> res = new ArrayList<>();
        place(0, n, board, new boolean[n], new boolean[2 * n], new boolean[2 * n], res);
        return res;
    }

    private void place(int r, int n, char[][] b, boolean[] cols, boolean[] d1, boolean[] d2, List<List<String>> res) {
        if (r == n) {
            List<String> sol = new ArrayList<>();
            for (char[] row : b) sol.add(new String(row));
            res.add(sol);
            return;
        }
        for (int c = 0; c < n; c++) {
            if (cols[c] || d1[r + c] || d2[r - c + n - 1]) continue;
            cols[c] = d1[r + c] = d2[r - c + n - 1] = true;
            b[r][c] = 'Q';
            place(r + 1, n, b, cols, d1, d2, res);
            b[r][c] = '.';
            cols[c] = d1[r + c] = d2[r - c + n - 1] = false;
        }
    }
}
