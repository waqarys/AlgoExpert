public class ProductSum {
    public static int productSum(List<Object> array) { return productSum(array, 1); }

    @SuppressWarnings("unchecked")
    private static int productSum(List<Object> array, int depth) {
        int sum = 0;
        for (Object o : array) sum += (o instanceof List) ? productSum((List<Object>) o, depth + 1) : (Integer) o;
        return sum * depth;
    }
}
