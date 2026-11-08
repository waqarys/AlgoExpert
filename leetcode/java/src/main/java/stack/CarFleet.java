package stack;

import java.util.*;

/**
 * LC 853 Car Fleet.
 * Approach: sort by position desc; a car whose solo arrival time exceeds the fleet ahead starts a new fleet.
 * Time O(n log n), Space O(n).
 */
public class CarFleet {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> position[b] - position[a]);
        int fleets = 0;
        double last = -1;
        for (int i : idx) {
            double t = (double) (target - position[i]) / speed[i];
            if (t > last) { fleets++; last = t; }
        }
        return fleets;
    }
}
