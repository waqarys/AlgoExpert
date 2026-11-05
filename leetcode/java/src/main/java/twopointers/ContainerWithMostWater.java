package twopointers;

/**
 * LC 11 Container With Most Water.
 * Approach: two pointers from the ends; always move the shorter wall inward.
 * Time O(n), Space O(1).
 */
public class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int l = 0, r = height.length - 1, best = 0;
        while (l < r) {
            best = Math.max(best, (r - l) * Math.min(height[l], height[r]));
            if (height[l] < height[r]) l++;
            else r--;
        }
        return best;
    }
}
