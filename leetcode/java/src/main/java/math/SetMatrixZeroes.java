package math;

/**
 * LC 73 Set Matrix Zeroes.
 * Approach: first row/column as markers plus two flags.
 * Time O(mn), Space O(1).
 */
public class SetMatrixZeroes {
    public void setZeroes(int[][] m) {
        int rows = m.length, cols = m[0].length;
        boolean firstRow = false, firstCol = false;
        for (int c = 0; c < cols; c++) if (m[0][c] == 0) firstRow = true;
        for (int r = 0; r < rows; r++) if (m[r][0] == 0) firstCol = true;
        for (int r = 1; r < rows; r++)
            for (int c = 1; c < cols; c++)
                if (m[r][c] == 0) { m[r][0] = 0; m[0][c] = 0; }
        for (int r = 1; r < rows; r++)
            for (int c = 1; c < cols; c++)
                if (m[r][0] == 0 || m[0][c] == 0) m[r][c] = 0;
        if (firstRow) for (int c = 0; c < cols; c++) m[0][c] = 0;
        if (firstCol) for (int r = 0; r < rows; r++) m[r][0] = 0;
    }
}
