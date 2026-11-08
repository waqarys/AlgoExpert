package greedy;

/**
 * LC 134 Gas Station.
 * Approach: one pass; reset start after any negative tank; feasible iff total >= 0.
 * Time O(n), Space O(1).
 */
public class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0, tank = 0, start = 0;
        for (int i = 0; i < gas.length; i++) {
            int d = gas[i] - cost[i];
            total += d;
            tank += d;
            if (tank < 0) { start = i + 1; tank = 0; }
        }
        return total < 0 ? -1 : start;
    }
}
