package com.smart.aop;

import org.slf4j.LoggerFactory;
import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.context.annotation.Bean;
import org.springframework.core.Ordered;
import org.springframework.stereotype.Component;

import java.util.Map;
import org.slf4j.Logger;

@Component
public class BeanSelfProxyAwareMounter implements SystemBootAddon, ApplicationContextAware {

    private ApplicationContext applicationContext;
    private Logger logger = LoggerFactory.getLogger(this.getClass());

    // 注入 Spring 容器
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        this.applicationContext = applicationContext;
    }

    public void onReady() { // 实现系统启动器接口中的装配就绪方法
        // 1 从容器中获取所有注入的自动代理 Bean
        Map<String, BeanSelfProxyAware> proxyAwareMap = applicationContext.getBeansOfType(BeanSelfProxyAware.class);
        if (proxyAwareMap != null) {
            for (BeanSelfProxyAware beanSelfProxyAware: proxyAwareMap.values()) {
                beanSelfProxyAware.setSelfProxy(beanSelfProxyAware);
                if (logger.isDebugEnabled()) {
                    logger.debug("{}注册自身被代理的实例");
                }
            }
        }

    }

    public int getOrder() {
        return Ordered.HIGHEST_PRECEDENCE;
    }
}
