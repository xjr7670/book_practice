public class Exercise11 {
    public static void main(String[] args) {
        final int seconds = 24 * 60 * 60 * 365;
        long total = 312032486L;
        for (int i = 0; i < 5; i++) {
            total += seconds / 7.0 - seconds / 13.0 + seconds / 45;           
            System.out.println(total);
        }
    }
}