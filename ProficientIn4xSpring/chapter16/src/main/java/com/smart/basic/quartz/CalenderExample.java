package com.smart.basic.quartz;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;
import org.quartz.impl.calendar.AnnualCalendar;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class CalenderExample {
    public static void main(String[] args) throws Exception {
        SchedulerFactory factory = new StdSchedulerFactory();
        Scheduler scheduler = factory.getScheduler();

        AnnualCalendar holidays = new AnnualCalendar(); // 法定节日以年为周期，所以使用 AnnualCalendar
        Calendar laborDay = new GregorianCalendar();    // 五一劳动节
        laborDay.add(Calendar.MONTH, 5);
        laborDay.add(Calendar.DATE, 1);

        Calendar nationalDay = new GregorianCalendar(); // 十一国庆节
        nationalDay.add(Calendar.MONTH, 10);
        nationalDay.add(Calendar.DATE, 1);

        ArrayList<Calendar> calendars = new ArrayList<Calendar>();
        calendars.add(laborDay);
        calendars.add(nationalDay);
        holidays.setDaysExcluded(calendars);            // 排除这两个日期

        scheduler.addCalendar("holidays", holidays, false, false);  // 向 Scheduler 注册日历

        Date runDate = TriggerUtils.getDateOf(0, 0, 10, 1, 4);  // 4 月 1 日上午 10 点
        JobDetail job = new JobDetail("job1", "group1", SimpleJob.class);
        SimpleTrigger trigger = new SimpleTrigger(
                "trigger1",
                "group1",
                runDate,
                null,
                SimpleTrigger.REPEAT_INDEFINITELY,
                60L * 60L * 1000L
        );
        trigger.setCalendarName("holidays");    // 让 Trigger 应用指定的日历规则
        scheduler.scheduleJob(job, trigger);
        scheduler.start();
    }
}
