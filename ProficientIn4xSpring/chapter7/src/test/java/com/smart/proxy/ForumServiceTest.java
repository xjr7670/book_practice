package com.smart.proxy;

import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;

import java.lang.reflect.Proxy;

public class ForumServiceTest {
    @Test
    public void proxy() {
        CglibProxy proxy = new CglibProxy();
        ForumServiceImpl forumService = (ForumServiceImpl) proxy.getProxy(ForumServiceImpl.class);
        forumService.removeForum(10);
        forumService.removeTopic(1023);
    }
}
