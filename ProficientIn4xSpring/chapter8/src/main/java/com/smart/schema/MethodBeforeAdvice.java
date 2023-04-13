package com.smart.schema;

import java.lang.reflect.Method;

public interface MethodBeforeAdvice {
    public void before(Method method, Object[] args, Object target) throws Throwable;
}
