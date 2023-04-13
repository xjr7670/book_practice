package com.smart.orm.dao;

import com.smart.orm.domain.Forum;

public class ForumDao extends BaseDao<Forum> {
    public long getForumNum() {
        Object obj = getHibernateTemplate().iterate(
                "select count(f.forumId) from Forum f"
        ).next();

        return (Long) obj;
    }
}
