# 0138. Copy List with Random Pointer

**Difficulty:** Medium | **Category:** Linked List | **LeetCode:** https://leetcode.com/problems/copy-list-with-random-pointer/

## Problem
- Each node has next and random (any node or null). Return a deep copy.

## Intuition
- The hard part is that random may point forward to a node not copied yet.
- Two passes with a map original -> copy: first create all copies, then wire next and random through the map.
- O(1)-space variant: interleave copies (A, A', B, B', ...), set random via orig.random.next, then unweave.

## Brute Force
- For each random, search by position from the head: O(n^2).

## Optimal Approach
1. Pass 1: map.put(node, new Node(node.val)).
2. Pass 2: copy.next = map.get(node.next); copy.random = map.get(node.random).
3. Return map.get(head).

## Worked Example
- [[7,null],[13,0],[11,4],[10,2],[1,0]] (val, random index).
```text
pass 1: 7' 13' 11' 10' 1'
pass 2: 13'.random = map(7) = 7'
        11'.random = map(1) = 1'
        10'.random = 11' ; 1'.random = 7'
```

## Complexity
- Time: O(n). Space: O(n) for the map (O(1) with interleaving).

## Pitfalls
- map.get(null) returns null, which conveniently handles null pointers.

## Video Script
- Show the map version first, then the interleaving trick as the "follow-up" answer.

## Solution
```java file=linkedlist/CopyListWithRandomPointer.java
package linkedlist;

import java.util.*;

/**
 * LC 138 Copy List with Random Pointer.
 * Approach: interleave copies after each original, set randoms, then separate. O(1) extra space.
 * Time O(n), Space O(1) (excluding output).
 */
public class CopyListWithRandomPointer {
    public static class Node {
        public int val;
        public Node next, random;
        public Node(int val) { this.val = val; }
    }

    public Node copyRandomList(Node head) {
        for (Node n = head; n != null; n = n.next.next) {
            Node c = new Node(n.val);
            c.next = n.next;
            n.next = c;
        }
        for (Node n = head; n != null; n = n.next.next)
            if (n.random != null) n.next.random = n.random.next;
        Node dummy = new Node(0), tail = dummy;
        for (Node n = head; n != null; n = n.next) {
            tail.next = n.next;
            tail = tail.next;
            n.next = n.next.next;
        }
        return dummy.next;
    }

    /** HashMap version: easiest to explain. */
    public Node copyWithMap(Node head) {
        Map<Node, Node> map = new HashMap<>();
        for (Node n = head; n != null; n = n.next) map.put(n, new Node(n.val));
        for (Node n = head; n != null; n = n.next) {
            map.get(n).next = map.get(n.next);
            map.get(n).random = map.get(n.random);
        }
        return map.get(head);
    }
}
```

## Tests
```java test=linkedlist/CopyListWithRandomPointerTest.java
package linkedlist;

import linkedlist.CopyListWithRandomPointer.Node;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class CopyListWithRandomPointerTest {
    static Node build(int[][] spec) {
        Node[] ns = new Node[spec.length];
        for (int i = 0; i < spec.length; i++) ns[i] = new Node(spec[i][0]);
        for (int i = 0; i < spec.length; i++) {
            if (i + 1 < spec.length) ns[i].next = ns[i + 1];
            if (spec[i][1] >= 0) ns[i].random = ns[spec[i][1]];
        }
        return spec.length == 0 ? null : ns[0];
    }
    static List<String> dump(Node h) {
        List<Node> order = new ArrayList<>();
        for (Node n = h; n != null; n = n.next) order.add(n);
        List<String> out = new ArrayList<>();
        for (Node n : order) out.add(n.val + ":" + (n.random == null ? -1 : order.indexOf(n.random)));
        return out;
    }
    int[][] spec = {{7, -1}, {13, 0}, {11, 4}, {10, 2}, {1, 0}};
    @Test void interleave() {
        Node h = build(spec);
        List<String> before = dump(h);
        Node c = new CopyListWithRandomPointer().copyRandomList(h);
        assertEquals(before, dump(c));
        assertEquals(before, dump(h)); // original restored
        assertNotSame(h, c);
        assertNotSame(h.next.random, c.next.random);
    }
    @Test void map() {
        Node h = build(spec);
        assertEquals(dump(h), dump(new CopyListWithRandomPointer().copyWithMap(h)));
        assertNull(new CopyListWithRandomPointer().copyRandomList(null));
    }
}
```
