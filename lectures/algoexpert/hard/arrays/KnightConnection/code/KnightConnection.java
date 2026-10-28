public class KnightConnection {
    public static int knightConnection(int[] a, int[] b) {
        int[][] mv = {{1, 2}, {2, 1}, {-1, 2}, {-2, 1}, {1, -2}, {2, -1}, {-1, -2}, {-2, -1}};
        ArrayDeque<int[]> q = new ArrayDeque<>();
        Set<Long> seen = new HashSet<>();
        q.add(new int[]{a[0], a[1], 0});
        seen.add(key(a[0], a[1]));
        while (true) {
            int[] c = q.poll();
            if (c[0] == b[0] && c[1] == b[1]) return (c[2] + 1) / 2;
            for (int[] m : mv) {
                int x = c[0] + m[0], y = c[1] + m[1];
                if (seen.add(key(x, y))) q.add(new int[]{x, y, c[2] + 1});
            }
        }
    }

    private static long key(int x, int y) { return ((long) x << 32) ^ (y & 0xffffffffL); }
}
