package com.smart.orm.dao.mybatis;

import com.smart.orm.domain.Forum;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Transactional
@Service
public class ForumMybatisDao {
    @Autowired
    private ForumMybatisDao forumDao;

    @Autowired
    private TopicMybatisDao topicDao;

    @Autowired
    private PostMybatisDao postDao;

    public void addForum(Forum forum) {
        forumDao.addForum(forum);
    }

    public void updateForum(Forum forum) {
        forumDao.updateForum(forum);
    }

    public Forum getForum(int forumId) {
        return forumDao.getForum(forumId);
    }

    public long getForumNum() {
        return 3L;
    }
}
