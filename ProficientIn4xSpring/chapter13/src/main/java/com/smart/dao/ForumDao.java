package com.smart.dao;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

import com.smart.domain.Forum;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.*;
import org.springframework.jdbc.support.GeneratedKeyHolder;
import org.springframework.jdbc.support.KeyHolder;
import org.springframework.stereotype.Repository;

// 1 声明一个 DAO
@Repository
public class ForumDao {
    private JdbcTemplate jdbcTemplate;

    @Autowired  // 2 注入 JdbcTemplate 实例
    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    public void initDb() {
        String sql = "create table t_user(user_id int primary key, user_name varchar(60))";
        jdbcTemplate.execute(sql);
    }

    public void addForum(final Forum forum) {
        String sql = "INSERT INTO t_forum(forum_name, forum_desc) VALUES (?, ?)";
        Object[] params = new Object[] {forum.getForumName(), forum.getForumDesc()};

        // 方式1
        jdbcTemplate.update(sql, params);

        // 方式2，指定参数类型
        // jdbcTemplate.update(sql, params, new int[]{Types.VARCHAR, Types.VARCHAR});

        // 方式3，通过匿名内部类定义回调实例
//        jdbcTemplate.update(sql, new PreparedStatementSetter() {
//            @Override
//            public void setValues(PreparedStatement preparedStatement) throws SQLException {
//                preparedStatement.setString(1, forum.getForumName());
//                preparedStatement.setString(2, forum.getForumDesc());
//            }
//        });

        // 方式4，使用 PreparedStatementCreator
//        jdbcTemplate.update(new PreparedStatementCreator() {
//            @Override
//            public PreparedStatement createPreparedStatement(Connection connection) throws SQLException {
//                PreparedStatement ps = connection.prepareStatement(sql);
//                ps.setString(1, forum.getForumName());
//                ps.setString(2, forum.getForumDesc());
//                return ps
//            }
//        });

        // 方式5
//        KeyHolder keyHolder = new GeneratedKeyHolder(); // 创建一个主键持有者
//        jdbcTemplate.update(new PreparedStatementCreator() {
//            @Override
//            public PreparedStatement createPreparedStatement(Connection connection) throws SQLException {
//                PreparedStatement ps = connection.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
//                ps.setString(1, forum.getForumName());
//                ps.setString(2, forum.getForumDesc());
//                return ps;
//            }
//        }, keyHolder);
//        forum.setForumId(keyHolder.getKey().intValue());
    }

    // 批量更新数据
    public void addForums(final List<Forum> forums) {
        final String sql = "INSERT INTO t_forum(forum_name, forum_desc) VALUES(?, ?)";
        jdbcTemplate.batchUpdate(sql, new BatchPreparedStatementSetter() {

            @Override
            public void setValues(PreparedStatement preparedStatement, int i) throws SQLException {
                Forum forum = forums.get(i);
                preparedStatement.setString(1, forum.getForumName());
                preparedStatement.setString(2, forum.getForumDesc());
            }

            // 指定该批的记录数
            @Override
            public int getBatchSize() {
                return forums.size();
            }
        });
    }

    // 查询数据
    public Forum getForum(final int forumId) {
        String sql = "SELECT forum_name, forum_desc FROM t_forum WHERE forum_id=?";
        final Forum forum = new Forum();

        // 将结果集数据行中的数据抽取到 forum 对象中
        jdbcTemplate.query(sql, new Object[]{forumId}, new RowCallbackHandler() {
            @Override
            public void processRow(ResultSet resultSet) throws SQLException {
                forum.setForumId(forumId);
                forum.setForumName(resultSet.getString("forum_name"));
                forum.setForumDesc(resultSet.getString("forum_desc"));
            }
        });
        return forum;
    }

    // 处理多条结果
    public List<Forum> getForums(final int fromId, final int toId) {
        String sql = "SELECT forum_id, forum_name, forum_desc FROM t_forum WHERE forum_id between ? and ?";
        final List forums = new ArrayList();

        jdbcTemplate.query(sql, new Object[]{fromId, toId}, new RowCallbackHandler() {
            @Override
            public void processRow(ResultSet resultSet) throws SQLException {
                Forum forum = new Forum();
                forum.setForumId(resultSet.getInt("forum_id"));
                forum.setForumName(resultSet.getString("forum_name"));
                forum.setForumDesc(resultSet.getString("forum_desc"));
                forums.add(forum);
            }
        });
        return forums;
    }

    // 使用 RowMapper 映射多行数据
    public List<Forum> getFormsByRM(final int fromId, final int toId) {
        String sql = "SELECT forum_id, forum_name, forum_desc FROM t_forum WHERE forum_id between ? and ?";

        return jdbcTemplate.query(sql, new Object[]{fromId, toId}, new RowMapper<Forum>() {
            @Override
            public Forum mapRow(ResultSet resultSet, int i) throws SQLException {
                Forum forum = new Forum();
                forum.setForumName(resultSet.getString("forum_name"));
                forum.setForumDesc(resultSet.getString("forum_desc"));
                forum.setForumId(resultSet.getInt("forum_id"));
                return forum;
            }
        });
    }
}
