public class TandemBicycle {
    public static int tandemBicycle(int[] red, int[] blue, boolean fastest) {
        Arrays.sort(red);
        Arrays.sort(blue);
        int n = red.length, total = 0;
        for (int i = 0; i < n; i++) {
            int b = fastest ? blue[n - 1 - i] : blue[i];
            total += Math.max(red[i], b);
        }
        return total;
    }
}
