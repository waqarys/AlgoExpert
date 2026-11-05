package binarysearch;

/**
 * LC 875 Koko Eating Bananas.
 * Approach: binary search the smallest speed k whose total hours <= h (monotonic predicate).
 * Time O(n log max), Space O(1).
 */
public class KokoEatingBananas {
    public int minEatingSpeed(int[] piles, int h) {
        int lo = 1, hi = 0;
        for (int p : piles) hi = Math.max(hi, p);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (hours(piles, mid) <= h) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private long hours(int[] piles, int k) {
        long total = 0;
        for (int p : piles) total += (p + (long) k - 1) / k;
        return total;
    }
}
