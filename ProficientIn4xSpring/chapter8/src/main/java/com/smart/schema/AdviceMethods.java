package com.smart.schema;

import org.aspectj.lang.ProceedingJoinPoint;

public class AdviceMethods {
    public void preGreeting() {
        System.out.println("--how are you!--");
    }
    public void postGreeting() {
        System.out.println("----see you soon--");
    }
    public void afterReturning(int retVal) {
        System.out.println("----beginAfterReturning----");
        System.out.println("Return: " + retVal);
        System.out.println("----afterAfterReturning----");
    }
    public void aroundMethod(ProceedingJoinPoint pjp) {
        System.out.println("---within aroundMethod---");
    }
    public void afterThrowingMethod(IllegalArgumentException iae) {
        // todo..
    }
    public void afterMethod() {
        System.out.println("----afterMethod----");
    }
    public void bindParams(int num, String name) {
        System.out.println("----bindParams()----");
        System.out.println("name: " + name);
        System.out.println("num: " + num);
        System.out.println("----bindParams()----");
    }
}
