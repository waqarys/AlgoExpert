public class LaptopRentals {
    public static int laptopRentals(int[][] times) {
        int[][] t = times.clone();
        Arrays.sort(t, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<Integer> ends = new PriorityQueue<>();
        for (int[] iv : t) {
            if (!ends.isEmpty() && ends.peek() <= iv[0]) ends.poll();
            ends.add(iv[1]);
        }
        return ends.size();
    }
}
