package com.smart.basic.quartz;

import org.quartz.JobDetail;
import org.quartz.Scheduler;
import org.quartz.SchedulerFactory;
import org.quartz.SimpleTrigger;
import org.quartz.impl.StdSchedulerFactory;

import java.util.Date;

public class SimpleTriggerRunner {
    public static void main(String[] args) {
        try {

            // 创建一个 JobDetail 实例，指定 SimpleJob
            JobDetail jobDetail = new JobDetail("job1_1", "jgroup1", SimpleJob.class);

            // 通过 SimpleTrigger 定义调度规则：马上启动，每2秒运行一次，共运行 100 次
            SimpleTrigger simpleTrigger = new SimpleTrigger("trigger1_1", "tgroup1");
            simpleTrigger.setStartTime(new Date());
            simpleTrigger.setRepeatInterval(2000);
            simpleTrigger.setRepeatCount(100);

            // 通过 SchedulerFactory 获取一个调度器实例
            SchedulerFactory schedulerFactory = new StdSchedulerFactory();
            Scheduler scheduler = schedulerFactory.getScheduler();

            // 注册并进行调度
            scheduler.scheduleJob(jobDetail, simpleTrigger);
            scheduler.start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
