package arrays;

import java.util.*;

/**
 * LC 128 Longest Consecutive Sequence.
 * Approach: HashSet; only start counting at x where x-1 is absent, then extend upward.
 * Time O(n), Space O(n).
 */
public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int x : nums) set.add(x);
        int best = 0;
        for (int x : set) {
            if (set.contains(x - 1)) continue;
            int y = x;
            while (set.contains(y + 1)) y++;
            best = Math.max(best, y - x + 1);
        }
        return best;
    }
}
