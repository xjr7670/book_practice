package com.smart.tagdepend;

import com.smart.attr.Car;

import java.util.*;

public class Boss {
    private com.smart.attr.Car car;
    private List favorites = new ArrayList();
    private Map jobs = new HashMap();
    private Properties mails = new Properties();
    private Map<String, Integer> jobTime = new HashMap<String, Integer>();

    public Map<String, Integer> getJobTime() {
        return this.jobTime;
    }

    public void setJobTime(Map<String, Integer> jobTime) {
        this.jobTime = jobTime;
    }

    public Properties getMails() {
        return this.mails;
    }

    public void setMails(Properties mails) {
        this.mails = mails;
    }

    public Map getJobs() {
        return this.jobs;
    }

    public void setJobs(Map jobs) {
        this.jobs = jobs;
    }

    public List getFavorites() {
        return this.favorites;
    }

    public void setFavorites(List favorites) {
        this.favorites = favorites;
    }

    // 设置 car 属性
    public void setCar(com.smart.attr.Car car) {
        this.car = car;
    }

    public Car getCar() {
        return this.car;
    }
}
