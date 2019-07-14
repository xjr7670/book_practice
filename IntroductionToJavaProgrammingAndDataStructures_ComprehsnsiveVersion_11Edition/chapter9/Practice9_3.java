import java.util.Date;

public class Practice9_3 {
    public static void main(String[] args) {
        Date d = null;
        for (int i = 4; i <= 11; i++) {
            long seconds = (long) Math.pow(10, i);
            d = new Date(seconds);
            System.out.println(d.toString());
        }
    }
}