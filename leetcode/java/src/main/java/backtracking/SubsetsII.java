package backtracking;

import java.util.*;

/**
 * LC 90 Subsets II.
 * Approach: sort, backtrack, skip equal values at the same recursion level.
 * Time O(n * 2^n), Space O(n).
 */
public class SubsetsII {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        List<List<Integer>> res = new ArrayList<>();
        dfs(a, 0, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] a, int start, List<Integer> path, List<List<Integer>> res) {
        res.add(new ArrayList<>(path));
        for (int i = start; i < a.length; i++) {
            if (i > start && a[i] == a[i - 1]) continue;
            path.add(a[i]);
            dfs(a, i + 1, path, res);
            path.remove(path.size() - 1);
        }
    }
}
