package com.smart.domain;

import com.smart.dao.BaseDao;
import com.smart.dao.Page;
import com.smart.domain.Post;
import org.springframework.stereotype.Repository;

@Repository
public class PostDao extends BaseDao<Post> {
    private static final String GET_PAGED_POSTS = "from Post where topic.topicId = ? order by createTime desc";
    private static final String DELETE_TOPIC_POSTS = "delete from Post where toopic.topicId = ?";

    public Page getPagedPosts(int topicId, int pageNo, int pageSize) {
        return pageQuery(GET_PAGED_POSTS, pageNo, pageSize, topicId);
    }

    public void deleteTopicPosts(int topicId) {
        getHibernateTemplate().bulkUpdate(DELETE_TOPIC_POSTS, topicId);
    }
}
