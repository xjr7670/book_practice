package com.smart.proxy;

public class ForumServiceImpl implements ForumService {

    public void removeTopic(int topicId) {
        System.out.println("模拟删除 Topic 记录：" + topicId);
        try {
            Thread.currentThread().sleep(20);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void removeForum(int forumId) {
        System.out.println("模拟删除 Forum 记录：" + forumId);
        try {
            Thread.currentThread().sleep(40);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        ForumServiceImpl forumService = new ForumServiceImpl();
    }
}
