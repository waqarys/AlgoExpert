package linkedlist;

/**
 * LC 287 Find the Duplicate Number.
 * Approach: treat i -> nums[i] as a linked list; Floyd's cycle entrance is the duplicate.
 * Time O(n), Space O(1).
 */
public class FindTheDuplicateNumber {
    public int findDuplicate(int[] nums) {
        int slow = 0, fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        slow = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
}
