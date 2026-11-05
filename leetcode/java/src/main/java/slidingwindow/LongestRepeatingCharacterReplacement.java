package slidingwindow;

/**
 * LC 424 Longest Repeating Character Replacement.
 * Approach: sliding window valid while length - maxFreq <= k; slide (not shrink) when invalid.
 * Time O(n), Space O(1).
 */
public class LongestRepeatingCharacterReplacement {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int l = 0, maxFreq = 0, best = 0;
        for (int r = 0; r < s.length(); r++) {
            maxFreq = Math.max(maxFreq, ++count[s.charAt(r) - 'A']);
            if (r - l + 1 - maxFreq > k) count[s.charAt(l++) - 'A']--;
            best = Math.max(best, r - l + 1);
        }
        return best;
    }
}
