package com.smart.conf;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConf {
    // 以下两个方法定义了两个 Bean，并提供了 Bean 的实例化逻辑
    @Bean
    public UserDao userDao() {
        return new UserDao();
    }
    @Bean
    public LogDao logDao() {
        return new LogDao();
    }

    // 定义了 logonService 的 Bean
    @Bean
    public LogonService logonService() {
        LogonService logonService = new LogonService();
        // 定前面定义的 Bean 注入 logonService Bean 中
        logonService.setLogDao(logDao());
        logonService.setUserDao(userDao());
        return logonService;
    }
}
