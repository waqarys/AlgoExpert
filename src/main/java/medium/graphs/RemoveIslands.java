package medium.graphs;

/**
 * <div class="html">
 * <p>
 *   You're given a two-dimensional array (a matrix) of potentially unequal height
 *   and width containing only <span>0</span>s and <span>1</span>s. The matrix
 *   represents a two-toned image, where each <span>1</span> represents black and
 *   each <span>0</span> represents white. An island is defined as any number of
 *   <span>1</span>s that are horizontally or vertically adjacent (but not
 *   diagonally adjacent) and that don't touch the border of the image. In other
 *   words, a group of horizontally or vertically adjacent <span>1</span>s isn't an
 *   island if any of those <span>1</span>s are in the first row, last row, first
 *   column, or last column of the input matrix.
 * </p>
 * <p>
 *   Note that an island can twist. In other words, it doesn't have to be a
 *   straight vertical line or a straight horizontal line; it can be L-shaped, for
 *   example.
 * </p>
 * <p>
 *   You can think of islands as patches of black that don't touch the border of
 *   the two-toned image.
 * </p>
 * <p>
 *   Write a function that returns a modified version of the input matrix, where
 *   all of the islands are removed. You remove an island by replacing it with
 *   <span>0</span>s.
 * </p>
 * <p>Naturally, you're allowed to mutate the input matrix.</p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">matrix</span> =
 * [
 *   [1, 0, 0, 0, 0, 0],
 *   [0, 1, 0, 1, 1, 1],
 *   [0, 0, 1, 0, 1, 0],
 *   [1, 1, 0, 0, 1, 0],
 *   [1, 0, 1, 1, 0, 0],
 *   [1, 0, 0, 0, 0, 1],
 * ]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>[
 *   [1, 0, 0, 0, 0, 0],
 *   [0, 0, 0, 1, 1, 1],
 *   [0, 0, 0, 0, 1, 0],
 *   [1, 1, 0, 0, 1, 0],
 *   [1, 0, 0, 0, 0, 0],
 *   [1, 0, 0, 0, 0, 1],
 * ]
 * <span class="CodeEditor-promptComment">// The islands that were removed can be clearly seen here:</span>
 * <span class="CodeEditor-promptComment">// [</span>
 * <span class="CodeEditor-promptComment">//   [ ,  ,  ,  ,  , ],</span>
 * <span class="CodeEditor-promptComment">//   [ , 1,  ,  ,  , ],</span>
 * <span class="CodeEditor-promptComment">//   [ ,  , 1,  ,  , ],</span>
 * <span class="CodeEditor-promptComment">//   [ ,  ,  ,  ,  , ],</span>
 * <span class="CodeEditor-promptComment">//   [ ,  , 1, 1,  , ],</span>
 * <span class="CodeEditor-promptComment">//   [ ,  ,  ,  ,  , ], </span>
 * <span class="CodeEditor-promptComment">// ]</span>
 * </pre>
 * </div>
 */
public class RemoveIslands {
}
