package com.smart.orm.dao.mybatis;

import com.smart.orm.domain.Forum;
import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class ForumMybatisTemplateDao {
    @Autowired
    private SqlSessionTemplate sessionTemplate;

    public Forum getForum(int forumId) {
        return (Forum) sessionTemplate.selectOne(
                "com.smart.orm.dao.mybatis.ForumMybatisDao.getForum",
                forumId
        );
    }

    public Forum getForum2(int forumId) {
        ForumMybatisDao forumMybatisDao = sessionTemplate.getMapper(ForumMybatisDao.class);
        return forumMybatisDao.getForum(forumId);
    }
}
