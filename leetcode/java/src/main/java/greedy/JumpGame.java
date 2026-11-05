package greedy;

/**
 * LC 55 Jump Game.
 * Approach: greedy farthest-reach scan.
 * Time O(n), Space O(1).
 */
public class JumpGame {
    public boolean canJump(int[] nums) {
        int reach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > reach) return false;
            reach = Math.max(reach, i + nums[i]);
        }
        return true;
    }
}
