    public static class DoublyLinkedList {
        public Node head, tail;

        public void setHead(Node n) {
            if (head == null) { head = tail = n; return; }
            insertBefore(head, n);
        }

        public void setTail(Node n) {
            if (tail == null) { setHead(n); return; }
            insertAfter(tail, n);
        }

        public void insertBefore(Node node, Node ins) {
            if (ins == head && ins == tail) return;
            remove(ins);
            ins.prev = node.prev;
            ins.next = node;
            if (node.prev == null) head = ins; else node.prev.next = ins;
            node.prev = ins;
        }
