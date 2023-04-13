package com.smart.anno;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.annotation.Resource;

@Component
public class Boss {
    private Car car;

    public Boss() {
        System.out.println("construct...");
    }

    @Autowired
    private void setCar(Car car) {
        System.out.println("execute in setCar");
        this.car = car;
    }

    @PostConstruct
    private void init1() {
        System.out.println("execute in init1");
    }

    @PostConstruct
    private void init2() {
        System.out.println("execute in init2");
    }

    @PreDestroy
    private void destroy1() {
        System.out.println("execute in destroy1");
    }

    @PreDestroy
    private void destroy2() {
        System.out.println("execute in destroy2");
    }
}
