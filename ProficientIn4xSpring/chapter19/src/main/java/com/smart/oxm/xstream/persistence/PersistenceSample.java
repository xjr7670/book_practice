package com.smart.oxm.xstream.persistence;

import com.smart.oxm.domain.User;
import com.thoughtworks.xstream.persistence.FilePersistenceStrategy;
import com.thoughtworks.xstream.persistence.PersistenceStrategy;
import com.thoughtworks.xstream.persistence.XmlArrayList;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class PersistenceSample {
    private static List<User> users;

    public void persist() {
        users = new ArrayList<User>();
        User user = new User();
        user.setUserId(1);
        user.setCredits(10);
        user.setUserName("tom");
        user.setPassword("123456");
        users.add(user);

        User user1 = new User();
        user1.setUserId(2);
        user1.setCredits(20);
        user1.setUserName("John");
        user1.setPassword("986324");
        user1.setLastIp("192.168.1.130");
        users.add(user1);

        // 创建持久化策略
        File file = new File("out");
        PersistenceStrategy strategy = new FilePersistenceStrategy(file);
        // 持久化集合对象
        List list = new XmlArrayList(strategy);
        list.addAll(users);
    }

    public static void main(String[] args) {
        PersistenceSample persistenceSample = new PersistenceSample();
        persistenceSample.persist();
    }
}
