package linkedlist;

import common.ListNode;

/**
 * LC 2 Add Two Numbers.
 * Approach: digit-by-digit addition with carry, continuing while any input or carry remains.
 * Time O(max(m,n)), Space O(max(m,n)).
 */
public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode a, ListNode b) {
        ListNode dummy = new ListNode(0), tail = dummy;
        int carry = 0;
        while (a != null || b != null || carry != 0) {
            int sum = carry;
            if (a != null) { sum += a.val; a = a.next; }
            if (b != null) { sum += b.val; b = b.next; }
            tail.next = new ListNode(sum % 10);
            tail = tail.next;
            carry = sum / 10;
        }
        return dummy.next;
    }
}
