package com.smart.orm.service.hibernate;

import com.smart.orm.dao.hibernate.PostHibernateDao;
import com.smart.orm.dao.hibernate.TopicHibernateDao;
import com.smart.orm.dao.hibraw.ForumHibernateDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Transactional
@Service
public class BbtForumService {
    @Autowired
    private ForumHibernateDao forumDao;

    @Autowired
    private TopicHibernateDao topicDao;

    @Autowired
    private PostHibernateDao postDao;
}
