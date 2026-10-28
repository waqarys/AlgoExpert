package medium.heaps;

import java.util.ArrayList;
import java.util.List;

/**
 * Min Heap Construction: array-backed min-heap with buildHeap (O(n) sift-down), siftUp, siftDown, peek,
 * insert and remove.
 * Time: build O(n), insert/remove O(log n), peek O(1) | Space: O(n).
 */
public class MinHeapConstruction {
    public static class MinHeap {
        public final List<Integer> heap;

        public MinHeap(List<Integer> array) { heap = buildHeap(new ArrayList<>(array)); }

        public List<Integer> buildHeap(List<Integer> a) {
            for (int i = (a.size() - 2) / 2; i >= 0; i--) siftDown(i, a.size() - 1, a);
            return a;
        }

        public void siftDown(int i, int end, List<Integer> h) {
            while (2 * i + 1 <= end) {
                int c = 2 * i + 1;
                if (c + 1 <= end && h.get(c + 1) < h.get(c)) c++;
                if (h.get(c) >= h.get(i)) return;
                java.util.Collections.swap(h, i, c);
                i = c;
            }
        }

        public void siftUp(int i, List<Integer> h) {
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
