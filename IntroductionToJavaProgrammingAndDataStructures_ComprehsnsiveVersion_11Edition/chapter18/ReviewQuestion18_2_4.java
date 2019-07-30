public class ReviewQuestion18_2_4 {
    public static void main(String[] args) {
        long num;

        num = getPow2(16);

        System.out.println(num);
    }

    public static long getPow2(int num) {
        if (num == 0) {
            return 1;
        } else {
            return 2 * getPow2(num - 1);
        }
    }
}