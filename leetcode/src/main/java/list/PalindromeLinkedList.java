package list;

import common.list.ListNode;

public class PalindromeLinkedList {
    public boolean isPalindrome(ListNode head) {
        if(head == null) return true;
        ListNode fast = head;
        ListNode slow = head;

        while(fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        ListNode tmp = reverseLinkedList(slow);

        while(tmp != null) {
            if(tmp.val != head.val) {
                return false;
            } else {
                tmp = tmp.next;
                head = head.next;
            }
        }

        return true;
    }

    private ListNode reverseLinkedList(ListNode root) {
        ListNode output = null;

        while(root != null) {
            ListNode tmp = root.next;
            root.next = output;
            output = root;
            root = tmp;
        }

        return output;
    }
}
