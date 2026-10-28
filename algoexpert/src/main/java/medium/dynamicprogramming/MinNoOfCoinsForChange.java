package medium.dynamicprogramming;

import java.util.Arrays;

/**
 * <div class="html">
 * <p>
 *   Given an array of positive integers representing coin denominations and a
 *   single non-negative integer <span>n</span> representing a target amount of
 *   money, write a function that returns the smallest number of coins needed to
 *   make change for (to sum up to) that target amount using the given coin
 *   denominations.
 * </p>
 * <p>
 *   Note that you have access to an unlimited amount of coins. In other words, if
 *   the denominations are <span>[1, 5, 10]</span>, you have access to an unlimited
 *   amount of <span>1</span>s, <span>5</span>s, and <span>10</span>s.
 * </p>
 * <p>
 *   If it's impossible to make change for the target amount, return
 *   <span>-1</span>.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">n</span> = 7
 * <span class="CodeEditor-promptParameter">denoms</span> = [1, 5, 10]
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>3 <span class="CodeEditor-promptComment">// 2x1 + 1x5</span>
 * </pre>
 * </div>
 */
public class MinNoOfCoinsForChange {

    public static void main(String[] args) {
        int[] input = {1, 5, 10};
        System.out.println(minNumberOfCoinsForChange(7, input) == 3);
    }

    public static int minNumberOfCoinsForChange(int n, int[] denoms) {
        int[] numOfCoins = new int[n + 1];
        Arrays.fill(numOfCoins, Integer.MAX_VALUE);
        numOfCoins[0] = 0;
        int toCompare = 0;
        for (int denom: denoms) {
            for (int amount = 0; amount < numOfCoins.length; amount++) {
                if (denom <= amount) {
                    if (numOfCoins[amount - denom] == Integer.MAX_VALUE) {
                        toCompare = numOfCoins[amount - denom];
                    } else {
                        toCompare = numOfCoins[amount - denom] + 1;
                    }
                    numOfCoins[amount] = Math.min(numOfCoins[amount], toCompare);
                }
            }
        }
        return numOfCoins[n] != Integer.MAX_VALUE ? numOfCoins[n] : -1;
    }
}
