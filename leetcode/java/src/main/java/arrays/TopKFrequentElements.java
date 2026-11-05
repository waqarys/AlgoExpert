package arrays;

import java.util.*;

/**
 * LC 347 Top K Frequent Elements.
 * Approach: count with a HashMap, then bucket sort by frequency (index = frequency).
 * Time O(n), Space O(n).
 */
public class TopKFrequentElements {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.merge(x, 1, Integer::sum);
        List<List<Integer>> bucket = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) bucket.add(new ArrayList<>());
        for (var e : freq.entrySet()) bucket.get(e.getValue()).add(e.getKey());
        int[] res = new int[k];
        int idx = 0;
        for (int f = nums.length; f >= 1 && idx < k; f--)
            for (int v : bucket.get(f)) {
                if (idx == k) break;
                res[idx++] = v;
            }
        return res;
    }
}
