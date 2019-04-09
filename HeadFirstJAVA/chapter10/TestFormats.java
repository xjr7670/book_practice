import java.util.Date;

public class TestFormats {
    public static void main(String[] args) {
        Date today = new Date();
        String ds = String.format("%tY%<tm%<td", today);
        System.out.println(ds);
        String s = String.format("I have %.2f, bugs to fix.", 476578.09876);
        System.out.println(s);
    }
}