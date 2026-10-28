public class BestSeat {
    public static int bestSeat(int[] seats) {
        int best = -1, bestGap = 0, l = 0;
        while (l < seats.length) {
            int r = l + 1;
            while (r < seats.length && seats[r] == 0) r++;
            int gap = r - l - 1;
            if (gap > bestGap) { bestGap = gap; best = (l + r) / 2; }
            l = r;
        }
        return best;
    }
}
