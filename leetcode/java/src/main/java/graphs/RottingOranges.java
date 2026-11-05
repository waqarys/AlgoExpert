package graphs;

import java.util.*;

/**
 * LC 994 Rotting Oranges.
 * Approach: multi-source BFS from all rotten oranges, one layer per minute.
 * Time O(mn), Space O(mn).
 */
public class RottingOranges {
    public int orangesRotting(int[][] g) {
        int m = g.length, n = g[0].length, fresh = 0, minutes = 0;
        Deque<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) {
                if (g[r][c] == 2) q.add(new int[]{r, c});
                else if (g[r][c] == 1) fresh++;
            }
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty() && fresh > 0) {
            for (int i = q.size(); i > 0; i--) {
                int[] cur = q.poll();
                for (int[] d : dirs) {
                    int r = cur[0] + d[0], c = cur[1] + d[1];
                    if (r < 0 || c < 0 || r >= m || c >= n || g[r][c] != 1) continue;
                    g[r][c] = 2;
                    fresh--;
                    q.add(new int[]{r, c});
                }
            }
            minutes++;
        }
        return fresh == 0 ? minutes : -1;
    }
}
