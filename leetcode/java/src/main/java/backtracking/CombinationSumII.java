package backtracking;

import java.util.*;

/**
 * LC 40 Combination Sum II.
 * Approach: sorted backtracking, each index used once, duplicates skipped per level.
 * Time O(n * 2^n), Space O(n).
 */
public class CombinationSumII {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        int[] c = candidates.clone();
        Arrays.sort(c);
        List<List<Integer>> res = new ArrayList<>();
        dfs(c, 0, target, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] c, int start, int rem, List<Integer> path, List<List<Integer>> res) {
        if (rem == 0) { res.add(new ArrayList<>(path)); return; }
        for (int i = start; i < c.length && c[i] <= rem; i++) {
            if (i > start && c[i] == c[i - 1]) continue;
            path.add(c[i]);
            dfs(c, i + 1, rem - c[i], path, res);
            path.remove(path.size() - 1);
        }
    }
}
