package com.smart.aspectj.example;

import com.smart.NaiveWaiter;
import com.smart.Waiter;
import com.smart.aspectj.aspectj.PreGreetingAspect;
import org.springframework.aop.aspectj.annotation.AspectJProxyFactory;
import org.testng.annotations.Test;

public class AspectJProxyTest {
    @Test
    public void proxy() {
        Waiter target = new NaiveWaiter();
        AspectJProxyFactory factory = new AspectJProxyFactory();
        // 1 设置目标对象
        factory.setTarget(target);
        // 2 添加切面类
        factory.addAspect(PreGreetingAspect.class);
        // 3 生成织入切面的代理对象
        Waiter proxy = factory.getProxy();
        proxy.greetTo("John");
        proxy.serveTo("John");
    }
}
