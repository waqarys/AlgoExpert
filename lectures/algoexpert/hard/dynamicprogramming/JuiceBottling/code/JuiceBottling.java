public class JuiceBottling {
    public static List<Integer> juiceBottling(int[] prices) {
        int n = prices.length;
        int[] best = new int[n], cut = new int[n];
        for (int s = 1; s < n; s++)
            for (int k = 1; k <= s; k++)
                if (prices[k] + best[s - k] > best[s]) { best[s] = prices[k] + best[s - k]; cut[s] = k; }
        List<Integer> out = new ArrayList<>();
        for (int s = n - 1; s > 0; s -= cut[s]) out.add(cut[s]);
        return out;
    }
}
