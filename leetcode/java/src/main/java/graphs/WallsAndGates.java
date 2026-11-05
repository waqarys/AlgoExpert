package graphs;

import java.util.*;

/**
 * LC 286 Walls and Gates.
 * Approach: multi-source BFS from every gate; first visit gives the nearest distance.
 * Time O(mn), Space O(mn).
 */
public class WallsAndGates {
    static final int INF = Integer.MAX_VALUE;

    public void wallsAndGates(int[][] rooms) {
        int m = rooms.length, n = rooms[0].length;
        Deque<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++) if (rooms[r][c] == 0) q.add(new int[]{r, c});
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int[] d : dirs) {
                int r = cur[0] + d[0], c = cur[1] + d[1];
                if (r < 0 || c < 0 || r >= m || c >= n || rooms[r][c] != INF) continue;
                rooms[r][c] = rooms[cur[0]][cur[1]] + 1;
                q.add(new int[]{r, c});
            }
        }
    }
}
