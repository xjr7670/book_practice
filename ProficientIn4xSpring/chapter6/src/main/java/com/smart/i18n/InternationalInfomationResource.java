package com.smart.i18n;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.util.GregorianCalendar;
import java.util.Locale;

public class InternationalInfomationResource {
    public static void main(String[] args) {
        String[] configs = { "com/smart/i18n/beans.xml" };
        ApplicationContext ctx = new ClassPathXmlApplicationContext(configs);

        Object[] params = { "John", new GregorianCalendar().getTime() };

        String str1 = ctx.getMessage("greeting.common", params, Locale.US);
        String str2 = ctx.getMessage("greeting.morning", params, Locale.CHINA);

        System.out.println(str1);
        System.out.println(str2);
    }
}
