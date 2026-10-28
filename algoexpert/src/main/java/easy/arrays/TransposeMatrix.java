package easy.arrays;

/**
 * Transpose Matrix: flip a 2D matrix over its main diagonal.
 * Time: O(w*h) | Space: O(w*h).
 */
public class TransposeMatrix {
    public static int[][] transposeMatrix(int[][] matrix) {
        int rows = matrix.length, cols = matrix[0].length;
        int[][] out = new int[cols][rows];
        for (int r = 0; r < rows; r++) for (int c = 0; c < cols; c++) out[c][r] = matrix[r][c];
        return out;
    }
}
