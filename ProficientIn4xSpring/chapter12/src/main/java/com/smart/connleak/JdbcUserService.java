package com.smart.connleak;

import com.smart.multithread.UserService;
import org.apache.commons.dbcp.BasicDataSource;
import org.springframework.aop.ThrowsAdvice;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DataSourceUtils;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.sql.Connection;

@Service("jdbcUserService")
public class JdbcUserService {
    private JdbcTemplate jdbcTemplate;

    @Autowired
    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @Transactional
    public void logon(String userName) {
        try {
            // 1 直接从数据源获取连接，后续程序没有显式释放该连接
//            Connection conn = jdbcTemplate.getDataSource().getConnection();
            // 使用 DataSourceUtils 获取数据连接
            Connection conn = DataSourceUtils.getConnection(jdbcTemplate.getDataSource());
            String sql = "UPDATE t_user SET last_logon_time=? WHERE user_name=?";
            jdbcTemplate.update(sql, System.currentTimeMillis(), userName);

            // 2 模拟程序代码的执行时间
            Thread.sleep(1000);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // 以异步线程的方式执行 JdbcUserService#logon() 方法，以模拟多线程的环境
    public static void asynchrLogon(JdbcUserService userService, String userName) {
        UserServiceRunner runner = new UserServiceRunner(userService, userName);
        runner.start();
    }
    private static class UserServiceRunner extends Thread {
        private JdbcUserService userService;
        private String userName;
        public UserServiceRunner(JdbcUserService userService, String userName) {
            this.userService = userService;
            this.userName = userName;
        }
        public void run() {
            userService.logon(userName);
        }
    }

    // 2 让主执行线程睡眠一段指定的时间
    public static void sleep(long time) {
        try {
            Thread.sleep(time);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    // 3 汇报数据源的连接占用情况
    public static void reportConn(BasicDataSource basicDataSource) {
        System.out.println("连接数 [active:idle]-[" + basicDataSource.getNumActive() + ": " + basicDataSource.getNumIdle() + "]");
    }

    public static void main(String[] args) {
        ApplicationContext ctx = new ClassPathXmlApplicationContext("com/smart/connleak/applicationContext.xml");
        JdbcUserService userService = (JdbcUserService) ctx.getBean("jdbcUserService");

        BasicDataSource basicDataSource = (BasicDataSource) ctx.getBean("dataSource");

        // 4 汇报数据源初始化连接占用情况
        JdbcUserService.reportConn(basicDataSource);

        JdbcUserService.asynchrLogon(userService, "tom");   // 启动一个异步线程 A
        JdbcUserService.sleep(500);

        // 5 此时线程 A 正在执行 JdbcUserService#logon() 方法
        JdbcUserService.reportConn(basicDataSource);
        JdbcUserService.sleep(2000);

        // 6 此时线程 A 所执行的 JdbcUserService#logon() 方法已经执行完毕
        JdbcUserService.reportConn(basicDataSource);

        JdbcUserService.asynchrLogon(userService, "john");  // 启动一个异步线程 B
        JdbcUserService.sleep(500);

        // 7 此时线程 B 正在执行 JdbcUserService#logon() 方法
        JdbcUserService.reportConn(basicDataSource);

        JdbcUserService.sleep(2000);

        // 8 此时线程 A 和 B 都已完成 JdbcUserService#logon() 方法的执行
        JdbcUserService.reportConn(basicDataSource);
    }
}
