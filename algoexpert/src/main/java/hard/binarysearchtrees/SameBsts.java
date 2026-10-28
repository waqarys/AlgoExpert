package hard.binarysearchtrees;

import java.util.List;

/**
 * Same BSTs: would inserting the two arrays (left to right) produce identical BSTs, without building them?
 * Recurse on first-smaller / first-greater-or-equal descendants within value bounds, using indices only.
 * Time: O(n^2) | Space: O(d).
 */
public class SameBsts {
    public static boolean sameBsts(List<Integer> a, List<Integer> b) {
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

    private static int bigger(List<Integer> x, int start, int max) {
        for (int i = start + 1; i < x.size(); i++) if (x.get(i) >= x.get(start) && x.get(i) < max) return i;
        return -1;
    }
}
