package com.smart.conf;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DaoConfig {
    @Bean
    public UserDao userDao() {
        return new UserDao();
    }
    @Bean
    public LogDao logDao() {
        return new LogDao();
    }
}
