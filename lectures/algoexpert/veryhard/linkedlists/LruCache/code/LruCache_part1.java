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
