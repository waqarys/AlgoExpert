public class SunsetViews {
    public static List<Integer> sunsetViews(int[] heights, String direction) {
        List<Integer> out = new ArrayList<>();
        boolean east = direction.equals("EAST");
        int max = Integer.MIN_VALUE;
        for (int k = 0; k < heights.length; k++) {
            int i = east ? heights.length - 1 - k : k;
            if (heights[i] > max) { out.add(i); max = heights[i]; }
        }
        if (east) Collections.reverse(out);
        return out;
    }
}
