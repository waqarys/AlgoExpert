package hard.heaps;

import java.util.Arrays;
import java.util.PriorityQueue;

/**
 * Laptop Rentals: given [start, end) rental intervals, minimum number of laptops needed so nobody waits.
 * Time: O(n log n) | Space: O(n).
 */
public class LaptopRentals {
    public static int laptopRentals(int[][] times) {
        int[][] t = times.clone();
        Arrays.sort(t, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<Integer> ends = new PriorityQueue<>();
        for (int[] iv : t) {
            if (!ends.isEmpty() && ends.peek() <= iv[0]) ends.poll();
            ends.add(iv[1]);
        }
        return ends.size();
    }
}
