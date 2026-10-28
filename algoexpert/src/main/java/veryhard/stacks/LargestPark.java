package veryhard.stacks;

import java.util.ArrayDeque;

/**
 * Largest Park: boolean matrix where false is free land and true is in use. Area of the largest all-free
 * rectangle (0 if none). For each row build a histogram of consecutive free cells above and take the
 * largest rectangle in it with a monotonic stack.
 * Time: O(w*h) | Space: O(w).
 */
public class LargestPark {
    public static int largestPark(boolean[][] land) {
        if (land.length == 0) return 0;
        int[] heights = new int[land[0].length];
        int best = 0;
        for (boolean[] row : land) {
            for (int c = 0; c < row.length; c++) heights[c] = row[c] ? 0 : heights[c] + 1;
            best = Math.max(best, largestRectangle(heights));
        }
        return best;
    }

    static int largestRectangle(int[] h) {
        ArrayDeque<Integer> st = new ArrayDeque<>();
        int best = 0;
        for (int i = 0; i <= h.length; i++) {
            int cur = i == h.length ? 0 : h[i];
            while (!st.isEmpty() && h[st.peek()] >= cur) {
                int height = h[st.pop()];
                int left = st.isEmpty() ? -1 : st.peek();
                best = Math.max(best, height * (i - left - 1));
            }
            st.push(i);
        }
        return best;
    }
}
