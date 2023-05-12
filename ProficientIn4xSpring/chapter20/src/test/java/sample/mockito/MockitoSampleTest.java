package sample.mockito;

import com.smart.domain.User;
import com.smart.service.UserService;
import com.smart.service.UserServiceImpl;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import static org.mockito.Mockito.*;
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotNull;

public class MockitoSampleTest {
    UserService mockUserService = mock(UserService.class);

    UserServiceImpl mockServiceImpl = mock(UserServiceImpl.class);

    @Mock
    User mockUser;

    @BeforeClass
    public void initMocks() {
        MockitoAnnotations.initMocks(this);
    }

    @Test
    public void testMockInterface() {
        when(mockUserService.findUserByUserName("tom")).thenReturn(new User("tom", "1234"));

        // 1-2 对方法设定返回值
        doReturn(true).when(mockServiceImpl).hasMatchUser("tom", "1234");

        // 1-3 对 void 方法进行方法预期设定
        User u = new User("John", "1234");
        doNothing().when(mockUserService).registerUser(u);

        // 1-4 执行方法调用
        User user = mockUserService.findUserByUserName("tom");
        boolean isMatch = mockUserService.hasMatchUser("tom", "1234");
        mockUserService.registerUser(u);

        assertNotNull(user);
        assertEquals(user.getUserName(), "tom");
        assertEquals(isMatch, true);

        verify(mockUserService).findUserByUserName("tom");
        verify(mockUserService, atLeastOnce()).findUserByUserName("tom");
        verify(mockUserService, atLeast(1)).findUserByUserName("tom");

        verify(mockUserService, atMost(1)).findUserByUserName("tom");
    }

    // 2 模拟实现类 UserServiceImpl 测试
    @Test
    public void testMockClass() {
        // 对方法设定返回值
        when(mockServiceImpl.findUserByUserName("tom")).thenReturn(new User("tom", "1234"));
        doReturn(true).when(mockServiceImpl).hasMatchUser("tom", "1234");

        User user = mockServiceImpl.findUserByUserName("tom");
        boolean isMatch = mockServiceImpl.hasMatchUser("tom", "1234");
        assertNotNull(user);
        assertEquals(user.getUserName(), "tom");
        assertEquals(isMatch, true);
    }

    // 3 模拟 User 类测试
    @Test
    public void testMockUser() {
        when(mockUser.getUserId()).thenReturn(1);
        when(mockUser.getUserName()).thenReturn("tom");
        assertEquals(mockUser.getUserName(), "tom");
        assertEquals(mockUser.getUserId(), 1);
    }


}
