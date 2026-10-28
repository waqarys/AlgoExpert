        public void remove(Node n) {
            if (n == head) head = head.next;
            if (n == tail) tail = tail.prev;
            if (n.prev != null) n.prev.next = n.next;
            if (n.next != null) n.next.prev = n.prev;
            n.prev = n.next = null;
        }

        public boolean containsNodeWithValue(int v) {
            for (Node c = head; c != null; c = c.next) if (c.value == v) return true;
            return false;
        }

        public java.util.List<Integer> values() {
            java.util.List<Integer> out = new java.util.ArrayList<>();
            for (Node c = head; c != null; c = c.next) out.add(c.value);
            return out;
        }
    }
}
