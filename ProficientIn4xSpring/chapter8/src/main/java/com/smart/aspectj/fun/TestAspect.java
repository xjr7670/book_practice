package com.smart.aspectj.fun;

import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.Aspect;

@Aspect
public class TestAspect {
    @AfterReturning("this(com.smart.Seller)")
    public void thisTest() {
        System.out.println("thisTest() executed!");
    }
}
