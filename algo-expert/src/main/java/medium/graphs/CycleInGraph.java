package medium.graphs;

import java.util.ArrayList;

/**
 * <div class="html">
 * <p>
 *   You're given a list of <span>edges</span> representing an unweighted, directed
 *   graph with at least one node. Write a function that returns a boolean
 *   representing whether the given graph contains a cycle.
 * </p>
 * <p>
 *   For the purpose of this question, a cycle is defined as any number of
 *   vertices, including just one vertex, that are connected in a closed chain. A
 *   cycle can also be defined as a chain of at least one vertex in which the first
 *   vertex is the same as the last.
 * </p>
 * <p>
 *   The given list is what's called an adjacency list, and it represents a graph.
 *   The number of vertices in the graph is equal to the length of
 *   <span>edges</span>, where each index <span>i</span> in
 *   <span>edges</span> contains vertex <span>i</span>'s outbound edges, in no
 *   particular order. Each individual edge is represented by a positive integer
 *   that denotes an index (a destination vertex) in the list that this vertex is
 *   connected to. Note that these edges are directed, meaning that you can only
 *   travel from a particular vertex to its destination, not the other way around
 *   (unless the destination vertex itself has an outbound edge to the original
 *   vertex).
 * </p>
 * <p>
 *   Also note that this graph may contain self-loops. A self-loop is an edge that
 *   has the same destination and origin; in other words, it's an edge that
 *   connects a vertex to itself. For the purpose of this question, a self-loop is
 *   considered a cycle.
 * </p>
 * <p>
 *   For a more detailed explanation, please refer to the Conceptual Overview
 *   section of this question's video explanation.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">edges</span> = [
 *   [1, 3],
 *   [2, 3, 4],
 *   [0],
 *   [],
 *   [2, 5],
 *   [],
 * ]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>true
 * <span class="CodeEditor-promptComment">// There are multiple cycles in this graph: </span>
 * <span class="CodeEditor-promptComment">// 1) 0 -&gt; 1 -&gt; 2 -&gt; 0</span>
 * <span class="CodeEditor-promptComment">// 2) 0 -&gt; 1 -&gt; 4 -&gt; 2 -&gt; 0</span>
 * <span class="CodeEditor-promptComment">// 3) 1 -&gt; 2 -&gt; 0 -&gt; 1</span>
 * <span class="CodeEditor-promptComment">// These are just 3 examples; there are more.</span>
 * </pre>
 * </div>
 */
public class CycleInGraph {
    public static void main(String[] args) {
        int[][] matrix = new int[][] {{0, -1, -3, 2, 0}, {1, -2, -5, -1, -3}, {3, 0, 0, -4, -1}};
        int expected = 3;
        int actual = new CycleInGraph().minimumPassesOfMatrix(matrix);
        assert (expected == actual);
    }

    public int minimumPassesOfMatrix(int[][] matrix) {
        int passes = convertNegatives(matrix);
        return (!containsNegative(matrix)) ? passes - 1 : -1;
    }

    public int convertNegatives(int[][] matrix) {
        ArrayList<int[]> queue = getAllPositivePositions(matrix);

        int passes = 0;

        while (queue.size() > 0) {
            int currentSize = queue.size();

            while (currentSize > 0) {
                int[] vals = queue.remove(0);
                int currentRow = vals[0];
                int currentCol = vals[1];

                ArrayList<int[]> adjacentPositions = getAdjacentPositions(currentRow, currentCol, matrix);
                for (int[] position :  adjacentPositions) {
                    int row = position[0];
                    int col = position[1];

                    int value = matrix[row][col];
                    if (value < 0) {
                        matrix[row][col] *= -1;
                        queue.add(new int[]{row, col});
                    }
                }

                currentSize -= 1;
            }

            passes += 1;
        }

        return passes;
    }

    public ArrayList<int[]> getAllPositivePositions(int[][] matrix) {
        ArrayList<int[]> positivePositions = new ArrayList<int[]>();

        for (int row = 0; row < matrix.length; row++) {
            for (int col = 0; col < matrix[row].length; col++) {
                int value = matrix[row][col];
                if (value > 0) {
                    positivePositions.add(new int[] {row, col});
                }
            }
        }

        return positivePositions;
    }

    public ArrayList<int[]> getAdjacentPositions(int row, int col, int[][] matrix) {
        ArrayList<int[]> adjacentPositions = new ArrayList<int[]>();

        if (row > 0) {
            adjacentPositions.add(new int[] {row - 1, col});
        }
        if (row < matrix.length - 1) {
            adjacentPositions.add(new int[] {row + 1, col});
        }
        if (col > 0) {
            adjacentPositions.add(new int[] {row, col - 1});
        }
        if (col < (matrix[0].length - 1)) {
            adjacentPositions.add(new int[] {row, col + 1});
        }

        return adjacentPositions;
    }

    public boolean containsNegative(int[][] matrix) {
        for (int[] row: matrix) {
            for (int value: row) {
                if (value < 0) {
                    return true;
                }
            }
        }

        return false;
    }
}
