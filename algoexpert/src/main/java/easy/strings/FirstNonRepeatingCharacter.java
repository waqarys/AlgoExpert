package easy.strings;

/**
 * First Non-Repeating Character: index of the first lowercase char occurring exactly once, else -1.
 * Time: O(n) | Space: O(1) (26 counters).
 */
public class FirstNonRepeatingCharacter {
    public static int firstNonRepeatingCharacter(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;
        for (int i = 0; i < s.length(); i++) if (freq[s.charAt(i) - 'a'] == 1) return i;
        return -1;
    }
}
