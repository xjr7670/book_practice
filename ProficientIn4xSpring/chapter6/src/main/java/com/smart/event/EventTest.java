package com.smart.event;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class EventTest {
    public static void main(String[] args) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext("com/smart/event/beans.xml");
        MailSender mailSender = (MailSender) ctx.getBean("mailSender");
        mailSender.sendMail("aaaa@bbb.com");
    }
}
