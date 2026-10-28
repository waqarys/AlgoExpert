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
