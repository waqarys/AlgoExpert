package veryhard.dynamicprogramming;

import java.util.*;

/**
 * Longest String Chain: a chain is built by removing one character at a time where every intermediate
 * string is in the input. Return the longest chain (length >= 2) from longest to shortest, or [].
 * Time: O(n * m^2 + n log n) | Space: O(n * m).
 */
public class LongestStringChain {
    public static List<String> longestStringChain(List<String> strings) {
        List<String> sorted = new ArrayList<>(strings);
        sorted.sort(Comparator.comparingInt(String::length));
        Map<String, Integer> len = new HashMap<>();
        Map<String, String> next = new HashMap<>();
        String bestStart = null;
        for (String s : sorted) {
            len.put(s, 1);
            for (int i = 0; i < s.length(); i++) {
                String shorter = s.substring(0, i) + s.substring(i + 1);
                if (len.containsKey(shorter) && len.get(shorter) + 1 > len.get(s)) { len.put(s, len.get(shorter) + 1); next.put(s, shorter); }
            }
            if (bestStart == null || len.get(s) > len.get(bestStart)) bestStart = s;
        }
        List<String> out = new ArrayList<>();
        if (bestStart == null || len.get(bestStart) < 2) return out;
        for (String s = bestStart; s != null; s = next.get(s)) out.add(s);
        return out;
    }
}
