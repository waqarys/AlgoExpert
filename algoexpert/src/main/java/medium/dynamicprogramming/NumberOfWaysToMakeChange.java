package medium.dynamicprogramming;

/**
 * Number Of Ways To Make Change: count combinations of unlimited coins that sum to n.
 * Time: O(n*d) | Space: O(n).
 */
public class NumberOfWaysToMakeChange {
    public static int numberOfWaysToMakeChange(int n, int[] denoms) {
        int[] ways = new int[n + 1];
        ways[0] = 1;
        for (int d : denoms) for (int a = d; a <= n; a++) ways[a] += ways[a - d];
        return ways[n];
    }
}
