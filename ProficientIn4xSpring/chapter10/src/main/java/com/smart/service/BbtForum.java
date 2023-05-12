package com.smart.service;

import org.springframework.transaction.annotation.Transactional;
import org.springframework.stereotype.Service;

@Service
@Transactional
public class BbtForum {
    public ForumDao forumDao;
    public TopicDao topicDao;
    public PostDao postDao;
    public void addTopic(Topic topic) throws Exception{
        topicDao.addTopic(topic);
        postDao.addPost(topic.getPost());
    }
    public Forum getForum(int forumId) {
        return forumDao.getForum(forumId);
    }
    public void updateForum(Forum forum) {
        forumDao.updateForum(forum);
    }
    public int getForumNum() {
        return forumDao.getForumNum();
    }
}
