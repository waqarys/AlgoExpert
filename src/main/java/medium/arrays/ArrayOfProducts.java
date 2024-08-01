package medium.arrays;

public class ArrayOfProducts {

    public static void main(String[] args) {
        var input = new int[] {5, 1, 4, 2};
        var expected = new int[] {8, 40, 10, 20};
        int[] actual = arrayOfProducts(input);
        System.out.println(expected.length == actual.length);
        for (int i = 0; i < actual.length; i++) {
            System.out.println(actual[i] == expected[i]);
        }
    }

    public static int[] arrayOfProducts(int[] array) {
        int[] products = new int[array.length];
        int[] leftProducts = new int[array.length];
        int[] rightProducts = new int[array.length];

        int leftRunningProduct = 1;
        for (int i = 0; i < array.length; i++) {
            leftProducts[i] = leftRunningProduct;
            leftRunningProduct *= array[i];
        }

        int rightRunningProduct = 1;
        for (int i = array.length - 1; i >= 0; i--) {
            rightProducts[i] = rightRunningProduct;
            rightRunningProduct *= array[i];
        }

        for (int i = 0; i < array.length; i++) {
            products[i] = leftProducts[i] * rightProducts[i];
        }

        return products;
    }
}
