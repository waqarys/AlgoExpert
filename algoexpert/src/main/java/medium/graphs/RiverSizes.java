package medium.graphs;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

/**
 * River Sizes: in a 0/1 matrix, sizes of all 4-directionally connected groups of 1s (any order).
 * Time: O(w*h) | Space: O(w*h).
 */
public class RiverSizes {
    public static List<Integer> riverSizes(int[][] m) {
        List<Integer> sizes = new ArrayList<>();
        boolean[][] seen = new boolean[m.length][m[0].length];
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int r = 0; r < m.length; r++)
            for (int c = 0; c < m[0].length; c++) {
                if (m[r][c] != 1 || seen[r][c]) continue;
                int size = 0;
                ArrayDeque<int[]> st = new ArrayDeque<>();
                st.push(new int[]{r, c});
                seen[r][c] = true;
                while (!st.isEmpty()) {
                    int[] p = st.pop();
                    size++;
                    for (int[] d : dirs) {
                        int nr = p[0] + d[0], nc = p[1] + d[1];
                        if (nr >= 0 && nc >= 0 && nr < m.length && nc < m[0].length && m[nr][nc] == 1 && !seen[nr][nc]) {
                            seen[nr][nc] = true;
                            st.push(new int[]{nr, nc});
                        }
                    }
                }
                sizes.add(size);
            }
        return sizes;
    }
}
