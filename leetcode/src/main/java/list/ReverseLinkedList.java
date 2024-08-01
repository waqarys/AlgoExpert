package list;

import common.list.ListNode;

public class ReverseLinkedList {

    public ListNode reverseList(ListNode head) {
        ListNode output = null;

        while(head != null) {
            ListNode tmp = head.next;
            head.next = output;
            output = head;
            head = tmp;
        }
        return output;
    }
}
