package linkedlist;

import common.ListNode;
import java.util.*;

/**
 * LC 23 Merge k Sorted Lists.
 * Approach: min-heap of current heads; pop smallest, push its successor.
 * Time O(N log k), Space O(k).
 */
public class MergeKSortedLists {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val));
        for (ListNode l : lists) if (l != null) pq.add(l);
        ListNode dummy = new ListNode(0), tail = dummy;
        while (!pq.isEmpty()) {
            ListNode n = pq.poll();
            tail.next = n;
            tail = n;
            if (n.next != null) pq.add(n.next);
        }
        return dummy.next;
    }
}
