public class SolveSudoku {
    public static int[][] solveSudoku(int[][] b) {
        int[] rows = new int[9], cols = new int[9], boxes = new int[9];
        for (int r = 0; r < 9; r++) for (int c = 0; c < 9; c++) if (b[r][c] != 0) {
            int bit = 1 << b[r][c];
            rows[r] |= bit; cols[c] |= bit; boxes[r / 3 * 3 + c / 3] |= bit;
        }
        solve(b, 0, rows, cols, boxes);
        return b;
    }
