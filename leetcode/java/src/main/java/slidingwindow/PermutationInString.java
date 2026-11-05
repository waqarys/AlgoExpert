package slidingwindow;

/**
 * LC 567 Permutation in String.
 * Approach: fixed-size window over s2 with letter counts; compare to s1's counts.
 * Time O(n), Space O(1).
 */
public class PermutationInString {
    public boolean checkInclusion(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        if (m > n) return false;
        int[] diff = new int[26]; // need - have
        for (int i = 0; i < m; i++) {
            diff[s1.charAt(i) - 'a']++;
            diff[s2.charAt(i) - 'a']--;
        }
        int zeros = 0;
        for (int d : diff) if (d == 0) zeros++;
        if (zeros == 26) return true;
        for (int r = m; r < n; r++) {
            zeros = update(diff, s2.charAt(r) - 'a', -1, zeros);
            zeros = update(diff, s2.charAt(r - m) - 'a', +1, zeros);
            if (zeros == 26) return true;
        }
        return false;
    }

    private int update(int[] diff, int c, int delta, int zeros) {
        if (diff[c] == 0) zeros--;
        diff[c] += delta;
        if (diff[c] == 0) zeros++;
        return zeros;
    }
}
