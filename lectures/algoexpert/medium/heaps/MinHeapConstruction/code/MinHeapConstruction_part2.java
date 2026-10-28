            while (i > 0 && h.get((i - 1) / 2) > h.get(i)) { java.util.Collections.swap(h, i, (i - 1) / 2); i = (i - 1) / 2; }
        }

        public int peek() { return heap.get(0); }

        public int remove() {
            java.util.Collections.swap(heap, 0, heap.size() - 1);
            int v = heap.remove(heap.size() - 1);
            siftDown(0, heap.size() - 1, heap);
            return v;
        }

        public void insert(int v) { heap.add(v); siftUp(heap.size() - 1, heap); }

        public boolean isEmpty() { return heap.isEmpty(); }
    }
}
