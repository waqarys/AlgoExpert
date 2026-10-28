package veryhard.famousalgorithms;

import java.util.*;

/**
 * A* Algorithm: shortest 4-directional path on a grid (0 free, 1 obstacle) from start to end using
 * Manhattan-distance heuristic. Returns the list of [row, col] positions, or [] if unreachable.
 * Time: O(w*h log(w*h)) | Space: O(w*h).
 */
public class AStarAlgorithm {
    public static int[][] aStarAlgorithm(int startRow, int startCol, int endRow, int endCol, int[][] graph) {
        int R = graph.length, C = graph[0].length;
        int[][] g = new int[R][C];
        for (int[] row : g) Arrays.fill(row, Integer.MAX_VALUE);
        int[][] from = new int[R * C][];
        PriorityQueue<int[]> open = new PriorityQueue<>(Comparator.comparingInt(x -> x[2]));
        g[startRow][startCol] = 0;
        open.add(new int[]{startRow, startCol, h(startRow, startCol, endRow, endCol)});
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!open.isEmpty()) {
            int[] cur = open.poll();
            int r = cur[0], c = cur[1];
            if (r == endRow && c == endCol) {
                LinkedList<int[]> path = new LinkedList<>();
                for (int[] p = {r, c}; p != null; p = from[p[0] * C + p[1]]) path.addFirst(p);
                return path.toArray(new int[0][]);
            }
            if (cur[2] > g[r][c] + h(r, c, endRow, endCol)) continue;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr < 0 || nc < 0 || nr >= R || nc >= C || graph[nr][nc] == 1) continue;
                if (g[r][c] + 1 < g[nr][nc]) {
                    g[nr][nc] = g[r][c] + 1;
                    from[nr * C + nc] = new int[]{r, c};
                    open.add(new int[]{nr, nc, g[nr][nc] + h(nr, nc, endRow, endCol)});
                }
            }
        }
        return new int[][]{};
    }

    private static int h(int r, int c, int er, int ec) { return Math.abs(r - er) + Math.abs(c - ec); }
}
