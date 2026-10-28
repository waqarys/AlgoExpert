package easy.greedyalgorithms;

import java.util.Arrays;

/**
 * Minimum Waiting Time: queries with durations run one at a time; choose an order minimising the total
 * time all queries spend waiting. Shortest-first is optimal.
 * Time: O(n log n) | Space: O(1).
 */
public class MinimumWaitingTime {
    public static int minimumWaitingTime(int[] queries) {
        Arrays.sort(queries);
        int total = 0;
        for (int i = 0; i < queries.length; i++) total += queries[i] * (queries.length - 1 - i);
        return total;
    }
}
