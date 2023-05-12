package com.smart.schema;

import com.smart.NaiveWaiter;
import com.smart.Seller;
import com.smart.SmartSeller;
import com.smart.Waiter;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.testng.annotations.Test;

public class SchemaTest {
    @Test
    public void schemaTest() {
        String configPath = "com/smart/schema/beans.xml";
        ApplicationContext ctx = new ClassPathXmlApplicationContext(configPath);
        Waiter naiveWaiter = (Waiter) ctx.getBean("naiveWaiter");
        Waiter naughtyWaiter = (Waiter) ctx.getBean("naughtyWaiter");
        naiveWaiter.greetTo("John");
        naughtyWaiter.greetTo("Tom");
        naiveWaiter.serveTo("John");
        SmartSeller smartSeller = (SmartSeller) ctx.getBean("smartSeller");
        smartSeller.sell("apple", "Tomas");

        ((Seller) naiveWaiter).sell("Beer", "John");

        ((NaiveWaiter) naiveWaiter).smile("John", 2);
    }
}
