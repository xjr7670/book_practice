package com.smart.service;

import com.smart.domain.LoginLogDao;
import com.smart.domain.User;
import com.smart.domain.UserDao;
import com.smart.exception.UserExistsException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    @Autowired
    private UserDao userDao;
    @Autowired
    private LoginLogDao loginLogDao;

    public void register(User user) throws UserExistsException {
        User u = this.getUserByUserName(user.getUserName());
        if (u != null) {
            throw new UserExistsException("用户名已存在");
        } else {
            user.setCredit(100);
            user.setUserType(1);
            userDao.save(user);
        }
    }

    public User getUserByUserName(String userName) {
        return userDao.getUserByUserName(userName);
    }

    public User getUserById(int userId) {
        return userDao.get(userId);
    }

    public void lockUser(String userName) {
        User user = userDao.getUserByUserName(userName);
        user.setLocked(User.USER_LOCK);
        userDao.update(user);
    }

    public void unlockUser(String userName) {
        User user = userDao.getUserByUserName(userName);
        user.setLocked(user.USER_UNLOCK);
        userDao.update(user);
    }

    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    public UserDao getUserDao() {
        return userDao;
    }

    public LoginLogDao getLoginLogDao() {
        return loginLogDao;
    }

    public void setLoginLogDao(LoginLogDao loginLogDao) {
        this.loginLogDao = loginLogDao;
    }
}
