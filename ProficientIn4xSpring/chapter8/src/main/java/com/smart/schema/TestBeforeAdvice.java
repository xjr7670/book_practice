package com.smart.schema;

import java.lang.reflect.Method;

public class TestBeforeAdvice implements MethodBeforeAdvice{
    @Override
    public void before(Method method, Object[] args, Object target) throws Throwable{
        System.out.println("------TestBeforeAdvice------");
        System.out.println("clientName:" + args[0]);
        System.out.println("------TestBeforeAdvice------");
    }
}
