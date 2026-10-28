public class MinimumWaitingTime {
    public static int minimumWaitingTime(int[] queries) {
        Arrays.sort(queries);
        int total = 0;
        for (int i = 0; i < queries.length; i++) total += queries[i] * (queries.length - 1 - i);
        return total;
    }
}
