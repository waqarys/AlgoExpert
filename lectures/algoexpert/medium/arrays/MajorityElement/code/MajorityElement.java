public class MajorityElement {
    public static int majorityElement(int[] a) {
        int cand = 0, count = 0;
        for (int x : a) {
            if (count == 0) cand = x;
            count += (x == cand) ? 1 : -1;
        }
        return cand;
    }
}
