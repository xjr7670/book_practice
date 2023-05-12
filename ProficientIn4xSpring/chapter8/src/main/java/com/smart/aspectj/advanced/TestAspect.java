package com.smart.aspectj.advanced;

import com.smart.Monitorable;
import org.aspectj.lang.annotation.*;

@Aspect
public class TestAspect {
    @AfterThrowing(value = "target(com.smart.SmartSeller)", throwing = "iae")
    public void bindException(IllegalArgumentException iae) {
        System.out.println("----bindException()----");
        System.out.println("exception: " + iae.getMessage());
        System.out.println("----bindException()----");
    }
}
