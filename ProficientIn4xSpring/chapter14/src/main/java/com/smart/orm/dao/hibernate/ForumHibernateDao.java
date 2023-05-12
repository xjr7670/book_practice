package com.smart.orm.dao.hibernate;

import com.smart.orm.domain.Forum;
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.springframework.orm.hibernate4.HibernateCallback;
import org.springframework.stereotype.Repository;

import javax.persistence.Lob;
import java.util.List;

@Repository
public class ForumHibernateDao extends BaseDao {
    public void addForum(Forum forum) {
        getHibernateTemplate().save(forum);
    }

    public void updateForum(Forum forum) {
        getHibernateTemplate().update(forum);
    }

    public Forum getForum(int forumId) {
        return getHibernateTemplate().get(Forum.class, forumId);
    }

    public List<Forum> findForumByName(String forumName) {  // 使用 HQL 查询
        return (List<Forum>) getHibernateTemplate().find("from Forum f where f.forumName like ?", forumName+"%");
    }

    public long getForumNum() { // 使用 Iterate 返回结果
        Object obj = getHibernateTemplate().iterate("select count(f.forumId) from Forum f").next();
        return (Long) obj;
    }

    public long getForumNum2() {
        Long forumNum = getHibernateTemplate().execute(
                new HibernateCallback<Long>() {
                    @Override
                    public Long doInHibernate(Session session) throws HibernateException {
                        Object obj = session.createQuery("select count(f.forumId) from Forum f")
                                .list()
                                .iterator()
                                .next();
                        return (Long) obj;
                    }
                }
        );
        return forumNum;
    }
}
