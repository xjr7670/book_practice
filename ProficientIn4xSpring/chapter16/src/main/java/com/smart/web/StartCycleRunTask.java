package com.smart.web;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class StartCycleRunTask implements ServletContextListener {
    private Timer timer;

    public void contextDestroyed(ServletContextEvent arg0) {
        System.out.println("Web 应用程序关闭...");
    }

    public void contextInitialized(ServletContextEvent arg0) {
        System.out.println("Web 应用程序启动...");
        timer = new Timer();
        TimerTask task = new SimpleTimerTask();
        timer.schedule(task, 1000L, 5000L);
    }
}

class SimpleTimerTask extends TimerTask {
    private int count;

    public void run() {
        System.out.println((++count) + "execute task..." + (new Date()));
    }
}
