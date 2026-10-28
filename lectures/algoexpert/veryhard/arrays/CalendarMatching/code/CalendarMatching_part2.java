    private static void addCal(List<int[]> busy, List<String[]> cal, String[] bounds) {
        busy.add(new int[]{0, min(bounds[0])});
        for (String[] m : cal) busy.add(new int[]{min(m[0]), min(m[1])});
        busy.add(new int[]{min(bounds[1]), 24 * 60});
    }

    private static int min(String t) { String[] p = t.split(":"); return Integer.parseInt(p[0]) * 60 + Integer.parseInt(p[1]); }

    private static String fmt(int m) { return (m / 60) + ":" + String.format("%02d", m % 60); }
}
