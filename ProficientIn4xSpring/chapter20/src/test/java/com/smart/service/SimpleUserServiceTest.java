package com.smart.service;

import org.testng.annotations.Test;
import org.unitils.spring.annotation.SpringBean;
import org.unitils.spring.annotation.SpringBeanByName;
import org.unitils.spring.annotation.SpringBeanByType;

import static org.testng.Assert.assertNotNull;

public class SimpleUserServiceTest extends BaseServiceTest {
    // spring 容器中加载 ID 为 userService 的 Bean
    @SpringBean("userService")
    private UserService userService1;

    // 从 spring 容器中加载与 userservice 相同类型的 bean
    @SpringBeanByType
    private UserService userService2;

    // 从 spring 容器中加载与 userservice 相同类型的 bean
    @SpringBeanByName
    private UserService userService;


    // 使用父类的 spring 应用上下文
    @Test
    public void testApplicationContext() {
        assertNotNull(applicationContext);
    }

    @Test
    public void testUserService() {
        assertNotNull(userService.findUserByUserName("tom"));
        assertNotNull(userService1.findUserByUserName("tom"));
        assertNotNull(userService2.findUserByUserName("tom"));
    }
}
