public class SpiralTraverse {
    public static List<Integer> spiralTraverse(int[][] m) {
        List<Integer> out = new ArrayList<>();
        if (m.length == 0) return out;
        int sr = 0, er = m.length - 1, sc = 0, ec = m[0].length - 1;
        while (sr <= er && sc <= ec) {
            for (int c = sc; c <= ec; c++) out.add(m[sr][c]);
            for (int r = sr + 1; r <= er; r++) out.add(m[r][ec]);
            for (int c = ec - 1; c >= sc && sr < er; c--) out.add(m[er][c]);
            for (int r = er - 1; r > sr && sc < ec; r--) out.add(m[r][sc]);
            sr++; er--; sc++; ec--;
        }
        return out;
    }
}
