package dp2;

import java.util.*;

/**
 * LC 62 Unique Paths.
 * Approach: grid DP compressed to one row: row[c] += row[c-1].
 * Time O(mn), Space O(n).
 */
public class UniquePaths {
    public int uniquePaths(int m, int n) {
        int[] row = new int[n];
        Arrays.fill(row, 1);
        for (int r = 1; r < m; r++)
            for (int c = 1; c < n; c++) row[c] += row[c - 1];
        return row[n - 1];
    }
}
