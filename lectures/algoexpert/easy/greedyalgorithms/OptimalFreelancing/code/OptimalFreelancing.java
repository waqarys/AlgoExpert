public class OptimalFreelancing {
    public static int optimalFreelancing(List<Map<String, Integer>> jobs) {
        final int days = 7;
        boolean[] taken = new boolean[days];
        int profit = 0;
        List<Map<String, Integer>> sorted = new java.util.ArrayList<>(jobs);
        sorted.sort((a, b) -> Integer.compare(b.get("payment"), a.get("payment")));
        for (Map<String, Integer> job : sorted) {
            for (int d = Math.min(job.get("deadline"), days) - 1; d >= 0; d--) {
                if (!taken[d]) { taken[d] = true; profit += job.get("payment"); break; }
            }
        }
        return profit;
    }
}
