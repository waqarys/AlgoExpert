package medium.graphs;

import java.util.ArrayDeque;

/**
 * Remove Islands: set to 0 every group of 1s not connected (4-directionally) to the matrix border.
 * Flood-fill from border 1s marking them, then clear the rest.
 * Time: O(w*h) | Space: O(w*h).
 */
public class RemoveIslands {
    public static int[][] removeIslands(int[][] m) {
        int R = m.length, C = m[0].length;
        ArrayDeque<int[]> st = new ArrayDeque<>();
        for (int r = 0; r < R; r++) for (int c = 0; c < C; c++)
            if ((r == 0 || c == 0 || r == R - 1 || c == C - 1) && m[r][c] == 1) { m[r][c] = 2; st.push(new int[]{r, c}); }
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!st.isEmpty()) {
            int[] p = st.pop();
            for (int[] d : dirs) {
                int r = p[0] + d[0], c = p[1] + d[1];
                if (r >= 0 && c >= 0 && r < R && c < C && m[r][c] == 1) { m[r][c] = 2; st.push(new int[]{r, c}); }
            }
        }
        for (int[] row : m) for (int c = 0; c < C; c++) row[c] = row[c] == 2 ? 1 : 0;
        return m;
    }
}
