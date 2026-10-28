public class LongestIncreasingSubsequence {
    public static List<Integer> longestIncreasingSubsequence(int[] a) {
        int n = a.length, len = 0;
        int[] tails = new int[n], prev = new int[n];
        for (int i = 0; i < n; i++) {
            int lo = 0, hi = len;
            while (lo < hi) { int m = (lo + hi) >>> 1; if (a[tails[m]] < a[i]) lo = m + 1; else hi = m; }
            prev[i] = lo > 0 ? tails[lo - 1] : -1;
            tails[lo] = i;
            if (lo == len) len++;
        }
        List<Integer> out = new ArrayList<>();
        for (int i = len == 0 ? -1 : tails[len - 1]; i != -1; i = prev[i]) out.add(a[i]);
        Collections.reverse(out);
        return out;
    }
}
