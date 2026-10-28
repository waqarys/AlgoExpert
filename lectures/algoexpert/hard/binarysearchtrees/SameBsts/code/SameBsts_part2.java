    private static int bigger(List<Integer> x, int start, int max) {
        for (int i = start + 1; i < x.size(); i++) if (x.get(i) >= x.get(start) && x.get(i) < max) return i;
        return -1;
    }
}
