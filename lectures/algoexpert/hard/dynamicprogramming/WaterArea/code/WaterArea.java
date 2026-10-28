public class WaterArea {
    public static int waterArea(int[] h) {
        int l = 0, r = h.length - 1, lMax = 0, rMax = 0, water = 0;
        while (l < r) {
            if (h[l] < h[r]) { lMax = Math.max(lMax, h[l]); water += lMax - h[l]; l++; }
            else { rMax = Math.max(rMax, h[r]); water += rMax - h[r]; r--; }
        }
        return water;
    }
}
