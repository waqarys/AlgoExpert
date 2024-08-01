package medium.dynamicprogramming;

/**
 * <div class="html">
 * <p>
 *   You're given two positive integers representing the width and height of a
 *   grid-shaped, rectangular graph. Write a function that returns the number of
 *   ways to reach the bottom right corner of the graph when starting at the top
 *   left corner. Each move you take must either go down or right. In other words,
 *   you can never move up or left in the graph.
 * </p>
 * <p>
 *   For example, given the graph illustrated below, with
 *   <span>width = 2</span> and <span>height = 3</span>, there are three ways to
 *   reach the bottom right corner when starting at the top left corner:
 * </p>
 * <pre>
 *  _ _
 * |_|_|
 * |_|_|
 * |_|_|
 * </pre>
 * <ol>
 *   <li>Down, Down, Right</li>
 *   <li>Right, Down, Down</li>
 *   <li>Down, Right, Down</li>
 * </ol>
 * <p>
 *   Note: you may assume that <span>width * height &gt;= 2</span>. In other words,
 *   the graph will never be a 1x1 grid.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">width</span> = 4
 * <span class="CodeEditor-promptParameter">height</span> = 3
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>10
 * </pre>
 * </div>
 */
public class NumberOfWaysToTraverseGraph {
    public static void main(String[] args) {
        int width = 4;
        int height = 3;
        int expected = 10;
        var actual = new NumberOfWaysToTraverseGraph().numberOfWaysToTraverseGraph(width, height);
        System.out.println(expected == actual);
    }

    //O(n + m) time | O(1) space
    //where :
    //  n  is the width of the graph and m is the height
    public int numberOfWaysToTraverseGraph(int width, int height) {
        int xDistanceToCorner = width - 1;
        int yDistanceToCorner = height - 1;

        //The number of permutations of right and down movements
        //is the number of ways to reach the bottom right corner.
        int numerator = factorial(xDistanceToCorner + yDistanceToCorner);
        int denominator = factorial(xDistanceToCorner) * factorial(yDistanceToCorner);
        return numerator / denominator;
    }

    public int factorial(int num) {
        int result = 1;

        for (int n = 2; n < num + 1; n++) {
            result *= n;
        }

        return result;
    }
}
