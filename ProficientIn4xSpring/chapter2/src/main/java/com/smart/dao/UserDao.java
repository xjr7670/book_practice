package com.smart.dao;

import com.smart.domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowCallbackHandler;
import org.springframework.stereotype.Repository;

import java.sql.ResultSet;
import java.sql.SQLException;

@Repository     // 通过 Spring 注解定义一个 DAO
public class UserDao {
    private JdbcTemplate jdbcTemplate;
    // 根据用户名查询用户的 SQL 语句
    private final static String MATCH_COUNT_SQL = " SELECT count(*) FROM t_user "
            + " WHERE user_name = ? AND password=?";
    private final static String UPDATE_LOGIN_INFO_SQL = " UPDATE t_user SET "
            + " last_visit=?, last_ip=?, credits=? WHERE user_id = ?";
    private final static String QUERY_BY_USERNAME = " SELECT user_id, user_name, credits "
            + " FROM t_user WHERE user_name = ? ";

    @Autowired     // 自动注入 JdbcTemplate 的 Bean
    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public int getMatchCount(String userName, String password) {
        return jdbcTemplate.queryForObject(MATCH_COUNT_SQL, new Object[]{userName, password}, Integer.class);
    }

    public User findUserByUserName(final String userName) {
        final User user = new User();
        jdbcTemplate.query(QUERY_BY_USERNAME, new Object[]{userName},
                new RowCallbackHandler() {
                    public void processRow(ResultSet resultSet) throws SQLException {
                        user.setUserId(resultSet.getInt("user_id"));
                        user.setUserName(userName);
                        user.setCredits(resultSet.getInt("credits"));
                    }
                }
        );

        return user;
    }

    public void updateLoginInfo(User user) {
        jdbcTemplate.update(UPDATE_LOGIN_INFO_SQL, user.getLastVisit(),
                user.getLastIp(), user.getCredits(), user.getUserId());
    }
}
