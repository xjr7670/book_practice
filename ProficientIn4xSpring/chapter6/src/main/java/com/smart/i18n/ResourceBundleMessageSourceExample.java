package com.smart.i18n;

import javafx.application.Application;
import org.springframework.context.ApplicationContext;
import org.springframework.context.MessageSource;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.util.GregorianCalendar;
import java.util.Locale;

public class ResourceBundleMessageSourceExample {
    public static void main(String[] args) {
        String[] configs = { "com/smart/i18n/beans.xml" };
        ApplicationContext ctx = new ClassPathXmlApplicationContext(configs);

        // 获取 MessageSource 的 Bean
        MessageSource ms = (MessageSource) ctx.getBean("myResource");
        Object[] params = { "John", new GregorianCalendar().getTime() };

        // 获取格式化的国际化信息
        String str1 = ms.getMessage("greeting.common", params, Locale.US);
        String str2 = ms.getMessage("greeting.morning", params, Locale.CHINA);
        String str3 = ms.getMessage("greeting.afternoon", params, Locale.CHINA);
        System.out.println(str1);
        System.out.println(str2);
        System.out.println(str3);
    }
}
