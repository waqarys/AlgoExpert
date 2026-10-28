package veryhard.linkedlists;

import java.util.HashMap;
import java.util.Map;

/**
 * LRU Cache: insertKeyValuePair, getValueFromKey (null if missing) and getMostRecentKey, evicting the
 * least recently used key at capacity. Hash map + doubly linked list.
 * Time: O(1) per op | Space: O(capacity).
 */
public class LruCache {
    private static class Node { String key; int value; Node prev, next; Node(String k, int v) { key = k; value = v; } }

    private final int capacity;
    private final Map<String, Node> map = new HashMap<>();
    private final Node head = new Node(null, 0), tail = new Node(null, 0);

    public LruCache(int capacity) {
        this.capacity = Math.max(1, capacity);
        head.next = tail; tail.prev = head;
    }

    public void insertKeyValuePair(String key, int value) {
        Node n = map.get(key);
        if (n != null) { n.value = value; moveToFront(n); return; }
        if (map.size() == capacity) { Node lru = tail.prev; unlink(lru); map.remove(lru.key); }
        n = new Node(key, value);
        map.put(key, n);
        addFront(n);
    }

    public Integer getValueFromKey(String key) {
        Node n = map.get(key);
        if (n == null) return null;
        moveToFront(n);
        return n.value;
    }

    public String getMostRecentKey() { return head.next == tail ? null : head.next.key; }

    private void moveToFront(Node n) { unlink(n); addFront(n); }
    private void unlink(Node n) { n.prev.next = n.next; n.next.prev = n.prev; }
    private void addFront(Node n) { n.next = head.next; n.prev = head; head.next.prev = n; head.next = n; }
}
