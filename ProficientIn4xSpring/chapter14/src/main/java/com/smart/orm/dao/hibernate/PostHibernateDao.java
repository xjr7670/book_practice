package com.smart.orm.dao.hibernate;

import com.smart.orm.domain.Post;
import org.springframework.stereotype.Repository;

@Repository
public class PostHibernateDao extends BaseDao {
    private void addPost(Post post) {
        getHibernateTemplate().save(post);
    }

    public Post getPost(int postId) {
        return null;
    }
}
