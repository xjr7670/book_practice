package com.smart.injectfun;

import org.springframework.beans.factory.support.MethodReplacer;

import java.lang.reflect.Method;

public class Boss2 implements MethodReplacer {
    public Object reimplement(Object arg0, Method arg1, Object[] arg2) throws Throwable {
        Car car = new Car();
        car.setBrand("美人豹");
        return car;
    }
}
