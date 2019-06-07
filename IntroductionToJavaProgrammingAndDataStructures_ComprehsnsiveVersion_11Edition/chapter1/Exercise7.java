public class Exercise7 {
    public static void main(String[] args) {
        int label = -1;
        double sum = 0;
        for (int i = 1; i <= 100000; i += 2) {
            label = label * -1;
            sum += label * (1.0 / i);
        }
        System.out.println(4 * sum);
    }
}