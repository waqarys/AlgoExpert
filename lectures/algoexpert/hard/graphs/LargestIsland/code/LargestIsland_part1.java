public class LargestIsland {
    public static int largestIsland(int[][] matrix) {
        int R = matrix.length, C = matrix[0].length, id = 2;
        int[][] m = new int[R][];
        for (int r = 0; r < R; r++) m[r] = matrix[r].clone();
        Map<Integer, Integer> size = new HashMap<>();
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int best = 0;
        for (int r = 0; r < R; r++) for (int c = 0; c < C; c++) {
            if (m[r][c] != 0) continue;
            int s = 0;
            ArrayDeque<int[]> st = new ArrayDeque<>();
            st.push(new int[]{r, c});
            m[r][c] = id;
            while (!st.isEmpty()) {
                int[] p = st.pop(); s++;
                for (int[] d : dirs) {
                    int nr = p[0] + d[0], nc = p[1] + d[1];
                    if (nr >= 0 && nc >= 0 && nr < R && nc < C && m[nr][nc] == 0) { m[nr][nc] = id; st.push(new int[]{nr, nc}); }
                }
            }
            size.put(id++, s);
