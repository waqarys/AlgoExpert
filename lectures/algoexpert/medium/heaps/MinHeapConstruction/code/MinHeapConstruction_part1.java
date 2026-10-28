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
