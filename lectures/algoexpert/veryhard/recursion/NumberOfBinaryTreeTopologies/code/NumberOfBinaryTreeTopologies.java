public class NumberOfBinaryTreeTopologies {
    public static long numberOfBinaryTreeTopologies(int n) {
        long[] c = new long[n + 1];
        c[0] = 1;
        for (int m = 1; m <= n; m++) for (int l = 0; l < m; l++) c[m] += c[l] * c[m - 1 - l];
        return c[n];
    }
}
