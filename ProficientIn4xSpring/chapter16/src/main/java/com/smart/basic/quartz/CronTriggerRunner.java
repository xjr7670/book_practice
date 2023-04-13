package com.smart.basic.quartz;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

public class CronTriggerRunner {
    public static void main(String[] args) {
        try {
            JobDetail jobDetail = new JobDetail("job1_2", "jGroup1", SimpleJob.class);

            CronTrigger cronTrigger = new CronTrigger("trigger1_2", "tgroup1");
            CronExpression cexp = new CronExpression("0/5 * * * * ?");
            cronTrigger.setCronExpression(cexp);

            SchedulerFactory schedulerFactory = new StdSchedulerFactory();
            Scheduler scheduler = schedulerFactory.getScheduler();
            scheduler.scheduleJob(jobDetail, cronTrigger);
            scheduler.start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
