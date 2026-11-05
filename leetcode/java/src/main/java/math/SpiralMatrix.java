package math;

import java.util.*;

/**
 * LC 54 Spiral Matrix.
 * Approach: shrink four boundaries after walking each side.
 * Time O(mn), Space O(1) extra.
 */
public class SpiralMatrix {
    public List<Integer> spiralOrder(int[][] m) {
        List<Integer> res = new ArrayList<>();
        int top = 0, bottom = m.length - 1, left = 0, right = m[0].length - 1;
        while (top <= bottom && left <= right) {
            for (int c = left; c <= right; c++) res.add(m[top][c]);
            top++;
            for (int r = top; r <= bottom; r++) res.add(m[r][right]);
            right--;
            if (top <= bottom) {
                for (int c = right; c >= left; c--) res.add(m[bottom][c]);
                bottom--;
            }
            if (left <= right) {
                for (int r = bottom; r >= top; r--) res.add(m[r][left]);
                left++;
            }
        }
        return res;
    }
}
