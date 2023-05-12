package com.smart.dao;

import com.smart.domain.User;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.unitils.UnitilsTestNG;
import org.unitils.dbunit.annotation.DataSet;
import org.unitils.dbunit.annotation.ExpectedDataSet;
import org.unitils.spring.annotation.SpringApplicationContext;
import org.unitils.spring.annotation.SpringBean;

import static com.smart.util.DateUtils.getDate;
import static org.junit.Assert.*;

@SpringApplicationContext({"smart-dao.xml"})
public class UserDaoTest extends UnitilsTestNG {
    @Test
    @DataSet
    public void getUser() {
        //todo...
    }

    @Test
    @ExpectedDataSet("UserDao.ExpectedSaveUser.xls")
    public void saveUser() throws Exception {
        User u = new User();
        u.setUserId(1);
        u.setUserName("tom");
        u.setPassword("123456");
        u.setLastVisit(getDate("2016-03-06 08:00:00", "yyyy-MM-dd HH:mm:ss"));
        u.setCredit(30);
        u.setLastIp("127.0.0.1");
        userDao.save(u);
    }

    @SpringBean("jdbcUserDao")
    private UserDao userDao;

    @BeforeClass
    public void init() {
        //todo..
    }

    @Test
    @DataSet("UserDao.Users.xls")
    public void findUserByUserName() {
        User user = userDao.findUserByUserName("tony");
        assertNull("不存在名为 tony 的用户！", user);
        user = userDao.findUserByUserName("jan");
        assertEquals("jan", user.getUserName());
        assertEquals("123456", user.getPassword());
        assertEquals(10, user.getCredit());
    }
}
