package medium.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * <div class="html">
 * <p>
 *   Write a function that takes in an n x m two-dimensional array (that can be
 *   square-shaped when n == m) and returns a one-dimensional array of all the
 *   array's elements in spiral order.
 * </p>
 * <p>
 *   Spiral order starts at the top left corner of the two-dimensional array, goes
 *   to the right, and proceeds in a spiral pattern all the way until every element
 *   has been visited.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">array</span> = [
 *   [1,   2,  3, 4],
 *   [12, 13, 14, 5],
 *   [11, 16, 15, 6],
 *   [10,  9,  8, 7],
 * ]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
 * </pre>
 * </div>
 */
public class SpiralTraverse {

    public static void main(String[] args) {
        var input =
                new int[][] {
                        {1, 2, 3, 4},
                        {12, 13, 14, 5},
                        {11, 16, 15, 6},
                        {10, 9, 8, 7},
                };
        var expected = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16);
        var actual = spiralTraverse(input);
        System.out.println(expected.equals(actual));
    }

    public static List<Integer> spiralTraverse(int[][] array) {
        if(array.length == 0) return new ArrayList<Integer>();

        var result = new ArrayList<Integer>();
        spiralFill(array, 0, array.length - 1, 0, array[0].length - 1, result);
        return result;
    }

    public static void spiralFill(
            int[][] array,
            int startRow,
            int endRow,
            int startCol,
            int endCol,
            ArrayList<Integer> result) {
        if(startRow > endRow || startCol > endCol) return;

        for (int col = startCol; col <= endCol; col++) {
            result.add(array[startRow][col]);
        }

        for (int row = startRow + 1; row <= endRow; row++) {
            result.add(array[row][endCol]);
        }

        for (int col = endCol - 1; col >= startCol; col--) {
            if(startRow == endRow) break;
            result.add(array[endRow][col]);
        }

        for (int row = endRow - 1; row >= startRow + 1; row--) {
            if(startCol == endCol) break;
            result.add(array[row][startCol]);
        }
        spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result);
    }
}
