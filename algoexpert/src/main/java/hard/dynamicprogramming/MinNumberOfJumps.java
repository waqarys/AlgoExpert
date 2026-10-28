package hard.dynamicprogramming;

/**
 * Min Number Of Jumps: each value is the max jump length from that index; fewest jumps to reach the end.
 * Greedy BFS-by-ranges.
 * Time: O(n) | Space: O(1).
 */
public class MinNumberOfJumps {
    public static int minNumberOfJumps(int[] a) {
        int jumps = 0, curEnd = 0, farthest = 0;
        for (int i = 0; i < a.length - 1; i++) {
            farthest = Math.max(farthest, i + a[i]);
            if (i == curEnd) { jumps++; curEnd = farthest; }
        }
        return jumps;
    }
}
