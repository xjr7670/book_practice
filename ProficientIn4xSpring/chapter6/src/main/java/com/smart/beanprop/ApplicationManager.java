package com.smart.beanprop;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class ApplicationManager {
    @Value("#{sysConfig.sessionTimeout}")
    private int sessionTimeout;

    @Value("#{sysConfig.maxTabPageNum}")
    private int maxTabPageNum;
}
