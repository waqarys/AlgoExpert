public class PalindromePartitioningMinCuts {
    public static int palindromePartitioningMinCuts(String s) {
        int n = s.length();
        boolean[][] pal = new boolean[n][n];
        int[] cuts = new int[n];
        for (int j = 0; j < n; j++) {
            cuts[j] = j;
            for (int i = 0; i <= j; i++)
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || pal[i + 1][j - 1])) {
                    pal[i][j] = true;
                    cuts[j] = i == 0 ? 0 : Math.min(cuts[j], cuts[i - 1] + 1);
                }
        }
        return n == 0 ? 0 : cuts[n - 1];
    }
}
