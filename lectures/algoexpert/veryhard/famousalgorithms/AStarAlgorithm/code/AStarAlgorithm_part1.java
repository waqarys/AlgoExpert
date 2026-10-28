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
