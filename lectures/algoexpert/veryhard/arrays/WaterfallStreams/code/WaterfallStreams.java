public class WaterfallStreams {
    public static double[] waterfallStreams(double[][] array, int source) {
        int w = array[0].length;
        double[] row = new double[w];
        row[source] = -1; // negative = water amount, to distinguish from blocks
        for (int r = 1; r < array.length; r++) {
            double[] cur = array[r].clone();
            for (int c = 0; c < w; c++) {
                double water = row[c];
                if (water >= 0) continue;
                if (cur[c] != 1.0) { cur[c] += water; continue; }
                double split = water / 2;
                for (int k = c - 1; k >= 0; k--) {
                    if (row[k] == 1.0) break;
                    if (cur[k] != 1.0) { cur[k] += split; break; }
                }
                for (int k = c + 1; k < w; k++) {
                    if (row[k] == 1.0) break;
                    if (cur[k] != 1.0) { cur[k] += split; break; }
                }
            }
            row = cur;
        }
        double[] out = new double[w];
        for (int c = 0; c < w; c++) out[c] = row[c] < 0 ? -row[c] * 100 : 0;
        return out;
    }
