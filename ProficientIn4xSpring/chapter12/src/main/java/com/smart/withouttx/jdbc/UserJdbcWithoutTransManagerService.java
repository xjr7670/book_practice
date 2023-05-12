package com.smart.withouttx.jdbc;

import org.apache.commons.dbcp.BasicDataSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

import java.util.Date;

@Service("userService")
public class UserJdbcWithoutTransManagerService {
    private JdbcTemplate jdbcTemplate;

    @Autowired
    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public void addScore(String userName, int toAdd) {
        String sql = "UPDATE t_user u SET u.credits = u.credits + ? WHERE user_name = ?";
        jdbcTemplate.update(sql, toAdd, userName);
    }

    public static void main(String[] args) {
        String configPath = "com/smart/withouttx/jdbc/jdbcWithoutTx.xml";
        ApplicationContext ctx = new ClassPathXmlApplicationContext(configPath);
        UserJdbcWithoutTransManagerService service = (UserJdbcWithoutTransManagerService) ctx.getBean("userService");
        JdbcTemplate jdbcTemplate = (JdbcTemplate) ctx.getBean("jdbcTemplate");
        BasicDataSource basicDataSource = (BasicDataSource) jdbcTemplate.getDataSource();

        // 1 检查数据源  autCommit 的设置
        System.out.println("autoCommit: " + basicDataSource.getDefaultAutoCommit());

        // 2 插入一条记录，初始分数为 10
        jdbcTemplate.execute("INSERT INTO t_user(user_name, password, credits, last_visit) " +
                "VALUES('tom', '123456', 10, '2020-05-02 11:41:36')");

        // 3 调用工作在无事务环境下的服务类方法，将分数添加 20 分
        service.addScore("tom", 20);

        // 4 查看此时用户的分数
        int score = jdbcTemplate.queryForObject(
                "SELECT credits FROM t_user WHERE user_name = 'tom'", Integer.class
        );
        System.out.println("score: " + score);
        jdbcTemplate.execute("DELETE FROM t_user WHERE user_name='tom'");
    }
}
