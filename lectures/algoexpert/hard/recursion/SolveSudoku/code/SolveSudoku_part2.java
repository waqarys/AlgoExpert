    private static boolean solve(int[][] b, int pos, int[] rows, int[] cols, int[] boxes) {
        if (pos == 81) return true;
        int r = pos / 9, c = pos % 9, bx = r / 3 * 3 + c / 3;
        if (b[r][c] != 0) return solve(b, pos + 1, rows, cols, boxes);
        for (int d = 1; d <= 9; d++) {
            int bit = 1 << d;
            if (((rows[r] | cols[c] | boxes[bx]) & bit) != 0) continue;
            b[r][c] = d; rows[r] |= bit; cols[c] |= bit; boxes[bx] |= bit;
            if (solve(b, pos + 1, rows, cols, boxes)) return true;
            b[r][c] = 0; rows[r] ^= bit; cols[c] ^= bit; boxes[bx] ^= bit;
        }
        return false;
    }
}
