public class ArrayOfProducts {
    public static int[] arrayOfProducts(int[] a) {
        int[] out = new int[a.length];
        int run = 1;
        for (int i = 0; i < a.length; i++) { out[i] = run; run *= a[i]; }
        run = 1;
        for (int i = a.length - 1; i >= 0; i--) { out[i] *= run; run *= a[i]; }
        return out;
    }
}
