package com.smart.dao;

import com.smart.domain.Forum;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.annotation.Rollback;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.testng.AbstractTransactionalTestNGSpringContextTests;
import org.springframework.transaction.annotation.Transactional;
import org.testng.annotations.Test;

import java.util.ArrayList;
import java.util.List;

@ContextConfiguration(locations = {"classpath:applicationContext.xml"})
@Rollback(false)
@Transactional
public class ForumDaoTest extends AbstractTransactionalTestNGSpringContextTests {

    @Autowired
    private ForumDao forumDao;

    @Test
    public void testInitDb() {
        forumDao.initDb();
    }

    @Test
    public void testAddForums() throws Throwable {
        List<Forum> forums = new ArrayList<Forum>();
        for (int i = 0; i < 10000; i++) {
            Forum f1 = new Forum();
            f1.setForumName("爱美妈妈");
            f1.setForumDesc("减肥、塑身、化妆品");
            forums.add(f1);
        }
        forumDao.addForums(forums);
    }

    @Test
    public void testAddForum() throws Throwable {
        Forum forum = new Forum();
        forum.setForumName("张十三");
        forum.setForumDesc("江湖侠客");
        forumDao.addForum(forum);
    }

    @Test
    public void testGetForum() {
        Forum forum = forumDao.getForum(10006);
        System.out.println(forum.getForumName());
        System.out.println(forum.getForumDesc());
    }
}
