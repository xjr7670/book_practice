package com.smart.service;

import com.smart.dao.LoginLogDao;
import com.smart.dao.UserDao;
import com.smart.domain.User;
import org.springframework.context.ApplicationContext;
import org.springframework.test.util.ReflectionTestUtils;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.unitils.UnitilsTestNG;
import org.unitils.dbunit.annotation.DataSet;
import org.unitils.spring.annotation.SpringApplicationContext;
import org.unitils.spring.annotation.SpringBean;

import java.util.Date;

import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.JMock1Matchers.equalTo;
import static org.junit.Assert.assertThat;
import static org.mockito.Mockito.*;
import static org.testng.Assert.assertNotNull;

@SpringApplicationContext({"smart-service.xml", "smart-dao.xml"})
public class UserServiceTest extends UnitilsTestNG {
    // 加载 spring 配置文件
    @SpringApplicationContext({"smart-service.xml", "smart-dao.xml"})
    private ApplicationContext applicationContext;

    // 加载 spring 容器中的 Bean
    @SpringBean("userService")
    private UserService userService;

    // 3 测试 spring 窗口中的用户服务 bean
    @Test
    public void testUserService() {
        assertNotNull(applicationContext);
        assertNotNull(userService.findUserByUserName("tom"));
    }

    private UserDao userDao;
    private LoginLogDao loginLogDao;

    @BeforeClass
    public void init() {
        userDao = mock(UserDao.class);
        loginLogDao = mock(LoginLogDao.class);
    }

    @Test
    public void findUserByUserName() {
        User user = new User();
        user.setUserName("tom");
        user.setPassword("1234");
        user.setCredit(100);
        doReturn(user).when(userDao).findUserByUserName("tom");

        UserServiceImpl userService = new UserServiceImpl();

        ReflectionTestUtils.setField(userService, "userDao", userDao);

        User u = userService.findUserByUserName("tom");
        assertNotNull(u);
        assertThat(u.getUserName(), equalTo(user.getUserName()));

        verify(userDao, times(1)).findUserByUserName("tom");
    }

    @Test
    @DataSet("Smart.SaveUsers.xls")
    public void loginSuccess() {
        User user = userService.findUserByUserName("tom");
        Date now = new Date();
        user.setLastVisit(now);
        userService.loginSuccess(user);
        User u = userService.findUserByUserName("tom");
        assertThat(u.getCredit(), is(105));
    }
}
