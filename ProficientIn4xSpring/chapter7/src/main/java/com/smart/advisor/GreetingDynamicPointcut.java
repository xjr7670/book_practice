package com.smart.advisor;

import org.springframework.aop.ClassFilter;
import org.springframework.aop.support.DynamicMethodMatcherPointcut;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;

public class GreetingDynamicPointcut extends DynamicMethodMatcherPointcut {
    private static List<String> specialClientList = new ArrayList<String>();
    static {
        specialClientList.add("John");
        specialClientList.add("Tom");
    }
    public ClassFilter getClassFilter() {
        return new ClassFilter() {
            @Override
            public boolean matches(Class<?> aClass) {
                System.out.println("调用 getClassFilter() 对 " + aClass.getName() + " 做静态检查。");
                return Waiter.class.isAssignableFrom(aClass);
            }
        };
    }

    public boolean matches(Method method, Class clazz) {
        System.out.println("调用 matches(method, clazz)" + clazz.getName() + "." + method.getName() + "做静态检查");
        return "greetTo".equals(method.getName());
    }

    public boolean matches(Method method, Class clazz, Object[] args) {
        System.out.println("调用 matches(method, clazz)" + clazz.getName() + "." + method.getName() + "做动态检查");
        String clientName = (String) args[0];
        return specialClientList.contains(clientName);
    }
}
