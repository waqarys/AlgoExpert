package twopointers;

/**
 * LC 42 Trapping Rain Water.
 * Approach: two pointers with running leftMax/rightMax; process the side with the lower bar.
 * Time O(n), Space O(1).
 */
public class TrappingRainWater {
    public int trap(int[] h) {
        int l = 0, r = h.length - 1, leftMax = 0, rightMax = 0, water = 0;
        while (l < r) {
            if (h[l] < h[r]) {
                leftMax = Math.max(leftMax, h[l]);
                water += leftMax - h[l++];
            } else {
                rightMax = Math.max(rightMax, h[r]);
                water += rightMax - h[r--];
            }
        }
        return water;
    }

    /** Prefix/suffix max version, O(n) space, easier to explain first. */
    public int trapArrays(int[] h) {
        int n = h.length, water = 0;
        if (n == 0) return 0;
        int[] left = new int[n], right = new int[n];
        left[0] = h[0];
        for (int i = 1; i < n; i++) left[i] = Math.max(left[i - 1], h[i]);
        right[n - 1] = h[n - 1];
        for (int i = n - 2; i >= 0; i--) right[i] = Math.max(right[i + 1], h[i]);
        for (int i = 0; i < n; i++) water += Math.min(left[i], right[i]) - h[i];
        return water;
    }
}
