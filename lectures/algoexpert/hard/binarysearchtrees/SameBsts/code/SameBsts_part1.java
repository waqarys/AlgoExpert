public class SameBsts {
    public static boolean sameBsts(List<Integer> a, List<Integer> b) {
        if (a.size() != b.size()) return false;
        if (a.isEmpty()) return true;
        return same(a, b, 0, 0, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private static boolean same(List<Integer> a, List<Integer> b, int ia, int ib, int min, int max) {
        if (ia == -1 || ib == -1) return ia == ib;
        if (!a.get(ia).equals(b.get(ib))) return false;
        int v = a.get(ia);
        return same(a, b, smaller(a, ia, min), smaller(b, ib, min), min, v)
                && same(a, b, bigger(a, ia, max), bigger(b, ib, max), v, max);
    }

    private static int smaller(List<Integer> x, int start, int min) {
        for (int i = start + 1; i < x.size(); i++) if (x.get(i) < x.get(start) && x.get(i) >= min) return i;
        return -1;
    }
