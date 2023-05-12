package com.smart.aspectj.advanced;

import com.smart.NaiveWaiter;
import com.smart.SmartSeller;
import com.smart.Waiter;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.testng.annotations.Test;

public class AdvancedTest {
    @Test
    public void advanced() {
        String configPath = "com/smart/aspectj/advanced/beans.xml";
        ApplicationContext ctx = new ClassPathXmlApplicationContext(configPath);
        SmartSeller seller = (SmartSeller) ctx.getBean("seller");
        seller.checkBill(2);
    }
}
