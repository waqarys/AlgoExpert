public class SweetAndSavory {
    public static int[] sweetAndSavory(int[] dishes, int target) {
        List<Integer> sweet = new ArrayList<>(), savory = new ArrayList<>();
        for (int d : dishes) if (d < 0) sweet.add(d); else if (d > 0) savory.add(d);
        sweet.sort(Collections.reverseOrder());
        Collections.sort(savory);
        int[] best = {0, 0};
        long bestDiff = Long.MAX_VALUE;
        int i = 0, j = 0;
        while (i < sweet.size() && j < savory.size()) {
            long sum = (long) sweet.get(i) + savory.get(j);
            if (sum <= target) {
                if (target - sum < bestDiff) { bestDiff = target - sum; best = new int[]{sweet.get(i), savory.get(j)}; }
                j++;
            } else i++;
        }
        return best;
    }
}
