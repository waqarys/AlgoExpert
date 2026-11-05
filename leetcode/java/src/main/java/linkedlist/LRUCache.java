package linkedlist;

import java.util.*;

/**
 * LC 146 LRU Cache.
 * Approach: HashMap key -> node + doubly linked list ordered by recency (sentinel head/tail).
 * O(1) get/put, Space O(capacity).
 */
public class LRUCache {
    private static class Node {
        int key, val;
        Node prev, next;
        Node(int k, int v) { key = k; val = v; }
    }

    private final int capacity;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node(0, 0), tail = new Node(0, 0);

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        Node n = map.get(key);
        if (n == null) return -1;
        unlink(n);
        addFront(n);
        return n.val;
    }

    public void put(int key, int value) {
        Node n = map.get(key);
        if (n != null) {
            n.val = value;
            unlink(n);
            addFront(n);
            return;
        }
        n = new Node(key, value);
        map.put(key, n);
        addFront(n);
        if (map.size() > capacity) {
            Node lru = tail.prev;
            unlink(lru);
            map.remove(lru.key);
        }
    }

    private void unlink(Node n) { n.prev.next = n.next; n.next.prev = n.prev; }

    private void addFront(Node n) {
        n.next = head.next;
        n.prev = head;
        head.next.prev = n;
        head.next = n;
    }
}
