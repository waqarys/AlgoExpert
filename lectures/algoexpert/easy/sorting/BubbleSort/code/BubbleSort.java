public class BubbleSort {
    public static int[] bubbleSort(int[] a) {
        boolean swapped = true;
        for (int end = a.length - 1; swapped && end > 0; end--) {
            swapped = false;
            for (int i = 0; i < end; i++)
                if (a[i] > a[i + 1]) { int t = a[i]; a[i] = a[i + 1]; a[i + 1] = t; swapped = true; }
        }
        return a;
    }
}
