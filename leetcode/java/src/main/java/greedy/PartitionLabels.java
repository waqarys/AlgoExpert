package greedy;

import java.util.*;

/**
 * LC 763 Partition Labels.
 * Approach: last-occurrence table; close a part when i reaches the furthest last index seen.
 * Time O(n), Space O(1).
 */
public class PartitionLabels {
    public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        for (int i = 0; i < s.length(); i++) last[s.charAt(i) - 'a'] = i;
        List<Integer> res = new ArrayList<>();
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            end = Math.max(end, last[s.charAt(i) - 'a']);
            if (i == end) { res.add(end - start + 1); start = i + 1; }
        }
        return res;
    }
}
