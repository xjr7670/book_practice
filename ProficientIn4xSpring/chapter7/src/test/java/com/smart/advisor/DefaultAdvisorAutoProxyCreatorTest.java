package com.smart.advisor;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.testng.annotations.Test;

public class DefaultAdvisorAutoProxyCreatorTest {
    @Test
    public void defaultAdvisorAutoProxyCreaotr() {
        String configPath = "com/smart/advisor/beans.xml";
        ApplicationContext context = new ClassPathXmlApplicationContext(configPath);
        Waiter waiter = (Waiter) context.getBean("waiter");
        Seller seller = (Seller) context.getBean("seller");
        waiter.greetTo("John");
        waiter.serveTo("John");
        seller.greetTo("Tom");
    }
}
