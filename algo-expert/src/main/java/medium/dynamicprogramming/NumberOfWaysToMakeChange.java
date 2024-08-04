package medium.dynamicprogramming;

/**
 * <div class="html">
 * <p>
 *   Given an array of distinct positive integers representing coin denominations and a
 *   single non-negative integer <span>n</span> representing a target amount of
 *   money, write a function that returns the number of ways to make change for
 *   that target amount using the given coin denominations.
 * </p>
 * <p>Note that an unlimited amount of coins is at your disposal.</p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">n</span> = 6
 * <span class="CodeEditor-promptParameter">denoms</span> = [1, 5]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>2 <span class="CodeEditor-promptComment">// 1x1 + 1x5 and 6x1</span>
 * </pre>
 * </div>
 */
public class NumberOfWaysToMakeChange {
    public static void main(String[] args) {
        int[] input = {1, 5};
        System.out.println(numberOfWaysToMakeChange(6, input) == 2);
    }

    // O(n) tim | O(n) space
    public static int numberOfWaysToMakeChange(int n, int[] denoms) {
        int[] ways = new int[n + 1];
        ways[0] = 1;
        for (int denom: denoms) {
            for (int amount = 1; amount < n + 1; amount++) {
                if (denom <= amount){
                    ways[amount] += ways[amount - denom];
                    System.out.println(ways[amount]);
                }
            }
        }
        return ways[n];
    }
}
