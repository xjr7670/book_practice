package com.smart.conf;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;

public class ServiceConfig {
    // 像普通 Bean 一样注入 DaoConfig
    @Autowired
    private DaoConfig daoConfig;

    @Bean
    public LogonService logonService() {
        LogonService logonService = new LogonService();

        // 像普通 Bean 一样，调用 Bean 相关的方法
        logonService.setLogDao(daoConfig.logDao());
        logonService.setUserDao(daoConfig.userDao());

        return logonService;
    }
}
