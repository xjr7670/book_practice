package com.smart.i18n;

import org.springframework.context.ApplicationContext;
import org.springframework.context.MessageSource;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.util.GregorianCalendar;
import java.util.Locale;

public class ReloadableResourceBundleMessageSourceExample {
    public static void main(String[] args) throws InterruptedException {
        String[] configs = { "com/smart/i18n/beans.xml" };
        ApplicationContext ctx = new ClassPathXmlApplicationContext(configs);

        MessageSource ms = (MessageSource) ctx.getBean("myResource1");
        Object[] params = { "John", new GregorianCalendar().getTime() };

        for (int i = 0; i < 5; i++) {
            String str1 = ms.getMessage("greeting.common", params, Locale.US);
            System.out.println(str1);
            Thread.currentThread().sleep(20000);
        }
    }
}
