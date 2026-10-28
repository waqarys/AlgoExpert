public class MinimumPassesOfMatrix {
    public static int minimumPassesOfMatrix(int[][] m) {
        ArrayDeque<int[]> q = new ArrayDeque<>();
        for (int r = 0; r < m.length; r++) for (int c = 0; c < m[0].length; c++) if (m[r][c] > 0) q.add(new int[]{r, c});
        int passes = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            int size = q.size();
            boolean flipped = false;
            for (int i = 0; i < size; i++) {
                int[] p = q.poll();
                for (int[] d : dirs) {
                    int r = p[0] + d[0], c = p[1] + d[1];
                    if (r >= 0 && c >= 0 && r < m.length && c < m[0].length && m[r][c] < 0) {
                        m[r][c] = -m[r][c]; q.add(new int[]{r, c}); flipped = true;
                    }
                }
            }
            if (flipped) passes++;
        }
        for (int[] row : m) for (int v : row) if (v < 0) return -1;
        return passes;
    }
