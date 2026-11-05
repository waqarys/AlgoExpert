package greedy;

/**
 * LC 45 Jump Game II.
 * Approach: greedy BFS over windows of indices reachable with the same jump count.
 * Time O(n), Space O(1).
 */
public class JumpGameII {
    public int jump(int[] nums) {
        int jumps = 0, end = 0, far = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            far = Math.max(far, i + nums[i]);
            if (i == end) { jumps++; end = far; }
        }
        return jumps;
    }
}
