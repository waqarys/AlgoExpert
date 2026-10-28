        public void insertAfter(Node node, Node ins) {
            if (ins == head && ins == tail) return;
            remove(ins);
            ins.prev = node;
            ins.next = node.next;
            if (node.next == null) tail = ins; else node.next.prev = ins;
            node.next = ins;
        }

        public void insertAtPosition(int pos, Node ins) {
            if (pos == 1) { setHead(ins); return; }
            Node cur = head;
            for (int p = 1; cur != null && p < pos; p++) cur = cur.next;
            if (cur != null) insertBefore(cur, ins); else setTail(ins);
        }

        public void removeNodesWithValue(int v) {
            Node cur = head;
            while (cur != null) { Node nx = cur.next; if (cur.value == v) remove(cur); cur = nx; }
        }
