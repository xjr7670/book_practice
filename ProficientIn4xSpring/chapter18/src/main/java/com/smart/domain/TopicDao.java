package com.smart.domain;

import com.smart.dao.BaseDao;
import com.smart.dao.Page;
import com.smart.domain.Topic;
import org.springframework.stereotype.Repository;

@Repository
public class TopicDao extends BaseDao<Topic> {
    private static final String GET_BOARD_DIGEST_TOPICS = "from Topic t where t.boardId = ? " +
            "and digest > 0 order by t.lastPost desc, digest desc";
    private static final String GET_PAGED_TOPICS = "from Topic where boardId = ? order by lastPost desc";
    private static final String QUERY_TOPIC_BY_TITLE = "from Topic where topicTitle like order by lastPost desc";

    // 获取论坛版块某一页的精华主题帖子，按最后回复时间及精华级别降序排列
    public Page getBoardDigestTopics(int boardId, int pageNo, int pageSize) {
        return pageQuery(GET_BOARD_DIGEST_TOPICS, pageNo, pageSize, boardId);
    }

    // 获取论坛版块某一页的主题帖子
    public Page getPagedTopics(int boardId, int pageNo, int pageSize) {
        return pageQuery(GET_PAGED_TOPICS, pageNo, pageSize, boardId);
    }

    // 3 获取和主题帖子标题模糊匹配的主题帖子（某一页的数据）
    public Page queryTopicByTitle(String title, int pageNo, int pageSize) {
        return pageQuery(QUERY_TOPIC_BY_TITLE, pageNo, pageSize, title);
    }
}
