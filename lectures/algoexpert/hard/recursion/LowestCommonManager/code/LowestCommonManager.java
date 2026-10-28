public class LowestCommonManager {
    public static class OrgChart {
        public final char name;
        public final List<OrgChart> directReports = new ArrayList<>();
        public OrgChart(char name) { this.name = name; }
        public OrgChart add(OrgChart... r) { directReports.addAll(List.of(r)); return this; }
    }

    public static OrgChart getLowestCommonManager(OrgChart top, OrgChart a, OrgChart b) {
        OrgChart[] ans = {null};
        count(top, a, b, ans);
        return ans[0];
    }

    private static int count(OrgChart m, OrgChart a, OrgChart b, OrgChart[] ans) {
        int n = (m == a ? 1 : 0) + (m == b ? 1 : 0);
        for (OrgChart r : m.directReports) { n += count(r, a, b, ans); if (ans[0] != null) return 2; }
        if (n == 2 && ans[0] == null) ans[0] = m;
        return n;
    }
}
