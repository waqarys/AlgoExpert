package backtracking;

import java.util.*;

/**
 * LC 39 Combination Sum.
 * Approach: sorted backtracking; recurse with the same index to allow reuse; break when too large.
 * Time exponential, Space O(target/min).
 */
public class CombinationSum {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        int[] c = candidates.clone();
        Arrays.sort(c);
        List<List<Integer>> res = new ArrayList<>();
        dfs(c, 0, target, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] c, int start, int rem, List<Integer> path, List<List<Integer>> res) {
        if (rem == 0) { res.add(new ArrayList<>(path)); return; }
        for (int i = start; i < c.length && c[i] <= rem; i++) {
            path.add(c[i]);
            dfs(c, i, rem - c[i], path, res);
            path.remove(path.size() - 1);
        }
    }
}
