package slidingwindow;

import java.util.*;

/**
 * LC 3 Longest Substring Without Repeating Characters.
 * Approach: sliding window; last-seen index lets the left edge jump past a repeat.
 * Time O(n), Space O(charset).
 */
public class LongestSubstringWithoutRepeating {
    public int lengthOfLongestSubstring(String s) {
        int[] last = new int[128];
        Arrays.fill(last, -1);
        int l = 0, best = 0;
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            if (last[c] >= l) l = last[c] + 1;
            last[c] = r;
            best = Math.max(best, r - l + 1);
        }
        return best;
    }
}
