package com.smart.anno;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Required;
import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Service;

// 定义一个 Service 的 Bean
@Service
public class LogonService {
    private LogDao logDao;
    private UserDao userDao;

    // 自动将 LogDao 传给方法入参
    @Lazy
    @Autowired(required = false)
    public void setLogDao(LogDao logDao) {
        this.logDao = logDao;
    }

    // 自动将名为 UserDao 的 Bean 传给方法入参
    @Autowired
    @Qualifier("userDao")
    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    @Autowired
    public void init(@Qualifier("userDao") UserDao userDao, LogDao logDao) {
        System.out.println("multi param inject");
        this.userDao = userDao;
        this.logDao = logDao;
    }
}
