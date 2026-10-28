package medium.recursion;

/**
 * Reveal Minesweeper: board of "M" (mine), "H" (hidden), "0"-"8" (revealed). Clicking a mine sets it to "X";
 * clicking a hidden cell reveals its adjacent-mine count and, if zero, recursively reveals neighbours.
 * Time: O(w*h) | Space: O(w*h).
 */
public class RevealMinesweeper {
    public static String[][] revealMinesweeper(String[][] board, int row, int col) {
        if (board[row][col].equals("M")) { board[row][col] = "X"; return board; }
        reveal(board, row, col);
        return board;
    }

    private static void reveal(String[][] b, int r, int c) {
        if (!b[r][c].equals("H")) return;
        int mines = 0;
        for (int dr = -1; dr <= 1; dr++) for (int dc = -1; dc <= 1; dc++) {
            int nr = r + dr, nc = c + dc;
            if ((dr != 0 || dc != 0) && nr >= 0 && nc >= 0 && nr < b.length && nc < b[0].length && b[nr][nc].equals("M")) mines++;
        }
        b[r][c] = String.valueOf(mines);
        if (mines > 0) return;
        for (int dr = -1; dr <= 1; dr++) for (int dc = -1; dc <= 1; dc++) {
            int nr = r + dr, nc = c + dc;
            if (nr >= 0 && nc >= 0 && nr < b.length && nc < b[0].length) reveal(b, nr, nc);
        }
    }
}
