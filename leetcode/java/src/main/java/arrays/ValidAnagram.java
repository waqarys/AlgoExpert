package arrays;

/**
 * LC 242 Valid Anagram. Is t a permutation of s?
 * Approach: 26-letter frequency array, +1 for s and -1 for t, all zeros means anagram.
 * Time O(n), Space O(1).
 */
public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        for (int c : count) if (c != 0) return false;
        return true;
    }
}
