import java.util.Calendar;
import java.util.Date;

public class UseCalendar {
    public static void main(String[] args) {
        Calendar c = Calendar.getInstance();
        c.set(2019, 3, 9, 11, 28);
        long day1 = c.getTimeInMillis();
        day1 += 1000 * 60 * 60;
        c.setTimeInMillis(day1);
        System.out.println("new hour " + c.get(c.HOUR_OF_DAY));
        c.add(c.DATE, 35);
        System.out.println("add 35 days " + c.getTime());
        // 滚动35天，只有日期字段滚动，月份不变
        c.roll(c.DATE, 35);
        System.out.println("roll 35 days " + c.getTime());
        // 直接设定DATE的值
        c.set(c.DATE, 1);
        System.out.println("set to 1 " + c.getTime());

        // 打印24小时制小时数
        System.out.println(c.get(Calendar.HOUR_OF_DAY));
        // 打印分钟
        System.out.println(c.get(Calendar.DAY_OF_YEAR));
        System.out.println(c.get(Calendar.MONTH));
        System.out.println(c.get(Calendar.YEAR));
    }
}