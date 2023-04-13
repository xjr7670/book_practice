package com.smart.dao;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

public class JdbcTemplateExample {
    public static void main(String[] args) {
        DriverManagerDataSource ds = new DriverManagerDataSource();
        ds.setDriverClassName("com.mysql.jdbc.Driver");
        ds.setUrl("jdbc:mysql://localhost:3306/sampledb");
        ds.setUsername("root");
        ds.setPassword("root");

        JdbcTemplate jdbcTemplate = new JdbcTemplate();
        jdbcTemplate.setDataSource(ds);

        String sql = "creata table t_user(user_id int primary key, user_name varchar(60))";
        jdbcTemplate.execute(sql);
    }
}
