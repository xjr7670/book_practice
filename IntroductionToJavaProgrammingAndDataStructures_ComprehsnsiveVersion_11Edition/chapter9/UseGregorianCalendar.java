import java.util.GregorianCalendar;

public class UseGregorianCalendar {
    public static void main(String[] args) {
        GregorianCalendar gCalendar = new GregorianCalendar();
        System.out.printf("当前年：%s，当前月：%s，当前日：%s\n", gCalendar.get(GregorianCalendar.YEAR), 
                                                             gCalendar.get(GregorianCalendar.MONTH)+1,
                                                             gCalendar.get(GregorianCalendar.DAY_OF_MONTH));

        GregorianCalendar gCalendar2 = new GregorianCalendar();
        gCalendar2.setTimeInMillis(1234567898765L);
        System.out.printf("当前年：%s，当前月：%s，当前日：%s\n", gCalendar2.get(GregorianCalendar.YEAR), 
                                                             gCalendar2.get(GregorianCalendar.MONTH),
                                                             gCalendar2.get(GregorianCalendar.DAY_OF_MONTH));        
    }
}