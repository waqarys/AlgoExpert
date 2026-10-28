public class CalendarMatching {
    public static List<String[]> calendarMatching(List<String[]> cal1, String[] bounds1, List<String[]> cal2, String[] bounds2, int duration) {
        List<int[]> busy = new ArrayList<>();
        addCal(busy, cal1, bounds1);
        addCal(busy, cal2, bounds2);
        busy.sort((a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> merged = new ArrayList<>();
        for (int[] b : busy) {
            if (!merged.isEmpty() && merged.get(merged.size() - 1)[1] >= b[0])
                merged.get(merged.size() - 1)[1] = Math.max(merged.get(merged.size() - 1)[1], b[1]);
            else merged.add(b.clone());
        }
        List<String[]> out = new ArrayList<>();
        for (int i = 1; i < merged.size(); i++) {
            int s = merged.get(i - 1)[1], e = merged.get(i)[0];
            if (e - s >= duration) out.add(new String[]{fmt(s), fmt(e)});
        }
        return out;
    }
