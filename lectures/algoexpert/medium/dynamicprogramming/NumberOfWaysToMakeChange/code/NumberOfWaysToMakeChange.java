public class NumberOfWaysToMakeChange {
    public static int numberOfWaysToMakeChange(int n, int[] denoms) {
        int[] ways = new int[n + 1];
        ways[0] = 1;
        for (int d : denoms) for (int a = d; a <= n; a++) ways[a] += ways[a - d];
        return ways[n];
    }
}
