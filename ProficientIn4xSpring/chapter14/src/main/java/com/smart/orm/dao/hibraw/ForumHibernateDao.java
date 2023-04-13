package com.smart.orm.dao.hibraw;

import com.smart.orm.domain.Forum;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;

public class ForumHibernateDao {
    // 1 直接注入 Hibernate 原生的 SessionFactory 对象
    @Autowired
    private SessionFactory sessionFactory;

    public void addForum(Forum forum) {
        sessionFactory.getCurrentSession().save(forum);
    }
    public void updateForum(Forum forum) {
        sessionFactory.getCurrentSession().update(forum);
    }
}
