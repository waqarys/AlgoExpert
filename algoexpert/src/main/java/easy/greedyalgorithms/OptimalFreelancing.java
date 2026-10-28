package easy.greedyalgorithms;

import java.util.List;
import java.util.Map;

/**
 * Optimal Freelancing: each job takes one day and has a deadline (days left) and a payment. Working at most
 * 7 days, one job per day, maximise profit. Greedy: take jobs by payment descending and place each in the
 * latest free day on or before its deadline.
 * Time: O(n log n) | Space: O(1) (7 slots).
 */
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
