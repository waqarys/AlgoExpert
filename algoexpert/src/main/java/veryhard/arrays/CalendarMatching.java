package veryhard.arrays;

import java.util.ArrayList;
import java.util.List;

/**
 * Calendar Matching: two people's meetings ("HH:MM" pairs) and daily bounds; return all free slots of at
 * least `duration` minutes available to both. Convert to minutes, merge busy intervals, invert.
 * Time: O(c1 + c2) | Space: O(c1 + c2).
 */
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

    private static void addCal(List<int[]> busy, List<String[]> cal, String[] bounds) {
        busy.add(new int[]{0, min(bounds[0])});
        for (String[] m : cal) busy.add(new int[]{min(m[0]), min(m[1])});
        busy.add(new int[]{min(bounds[1]), 24 * 60});
    }

    private static int min(String t) { String[] p = t.split(":"); return Integer.parseInt(p[0]) * 60 + Integer.parseInt(p[1]); }

    private static String fmt(int m) { return (m / 60) + ":" + String.format("%02d", m % 60); }
}
