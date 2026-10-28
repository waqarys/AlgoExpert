public class MaxSumIncreasingSubsequence {
    public static List<List<Integer>> maxSumIncreasingSubsequence(int[] a) {
        int n = a.length, bestIdx = 0;
        int[] sums = a.clone(), prev = new int[n];
        for (int i = 0; i < n; i++) {
            prev[i] = -1;
            for (int j = 0; j < i; j++)
                if (a[j] < a[i] && sums[j] + a[i] > sums[i]) { sums[i] = sums[j] + a[i]; prev[i] = j; }
            if (sums[i] > sums[bestIdx]) bestIdx = i;
        }
        List<Integer> seq = new ArrayList<>();
        for (int i = bestIdx; i != -1; i = prev[i]) seq.add(a[i]);
        Collections.reverse(seq);
        return List.of(List.of(sums[bestIdx]), seq);
    }
}
