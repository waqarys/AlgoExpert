public class NumbersInPi {
    public static int numbersInPi(String pi, String[] numbers) {
        Set<String> set = new HashSet<>(Arrays.asList(numbers));
        int n = pi.length();
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[n] = -1;
        for (int i = n - 1; i >= 0; i--)
            for (int j = i + 1; j <= n; j++)
                if (dp[j] != Integer.MAX_VALUE && set.contains(pi.substring(i, j))) dp[i] = Math.min(dp[i], dp[j] + 1);
        return dp[0] == Integer.MAX_VALUE ? -1 : dp[0];
    }
}
