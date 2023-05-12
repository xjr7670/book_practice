package com.smart.quartz;

import org.quartz.Job;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;
import org.springframework.context.ApplicationContext;

import java.util.Map;

public class MyJob implements Job {
    @Override
    public void execute(JobExecutionContext jobExecutionContext) throws JobExecutionException {
        Map dataMap = jobExecutionContext.getJobDetail().getJobDataMap();
        String size = (String) dataMap.get("size");

        ApplicationContext ctx = (ApplicationContext) dataMap.get("applicationContext");
        System.out.println("size: " + size);
        dataMap.put("size", size + "0");
    }
}
