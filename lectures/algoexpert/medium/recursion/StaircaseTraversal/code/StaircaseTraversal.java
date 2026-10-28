public class StaircaseTraversal {
    public static int staircaseTraversal(int height, int maxSteps) {
        int[] ways = new int[height + 1];
        ways[0] = 1;
        int window = 0;
        for (int h = 1; h <= height; h++) {
            window += ways[h - 1];
            if (h - maxSteps - 1 >= 0) window -= ways[h - maxSteps - 1];
            ways[h] = window;
        }
        return ways[height];
    }
}
