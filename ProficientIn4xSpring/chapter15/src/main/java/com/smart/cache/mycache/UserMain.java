package com.smart.cache.mycache;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class UserMain {
    public static void main(String[] args) {

        ApplicationContext ctx = new ClassPathXmlApplicationContext("applicationContext.xml");
        UserService userService = (UserService) ctx.getBean("userServiceBean");

        // 开始查询账号
        System.out.println("first query...");
        userService.getUserById("somebody");  // 第1次查询，应该是数据库查询
        System.out.println("second query...");
        userService.getUserById("somebody");  // 第2次查询，应该直接从缓存返回
    }
}
