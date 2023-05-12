package com.smart.injectfun;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.testng.annotations.Test;

public class MethodReplaceTest {
    @Test
    public void replace() {
        ClassPathXmlApplicationContext pFactory = new ClassPathXmlApplicationContext(new String[] {"com/smart/injectfun/beans1.xml"});
        Boss1 boss1 = (Boss1) pFactory.getBean("boss1");
        System.out.println(boss1.getCar().toString());
    }
}
