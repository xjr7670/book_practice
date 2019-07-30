public class ComputeFactorialTailRecursion {
    public static long factorial(int n) {
        return fatorial(n, 1);
    }

    private static long factorial(int n, int result) {
        if (n == 0) {
            return result;
        } else {
            return factorial(n - 1, n * result);
        }
    }
}