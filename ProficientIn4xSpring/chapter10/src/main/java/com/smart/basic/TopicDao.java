package com.smart.basic;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

public class TopicDao {
    // 1 使用 ThreadLocal 保存 Connection 变量
    private static ThreadLocal<Connection> connThreadLocal= new ThreadLocal<Connection>();
    public static Connection getConnection() {
        // 2 如果 connThreadLocal 没有本线程对应的 Connection，则创建一个新的 Connection，并将其保存到线程本地变量中
        if (connThreadLocal.get() == null) {
            Connection conn = ConnectionManager.getConnection();
            connThreadLocal.set(conn);
            return conn;
        } else {
            // 直接返回线程本地变量
            return connThreadLocal.get();
        }
    }
    public void addTopic() throws SQLException {
        // 4 从 ThreadLocal 中获取线程对应的 Connection
        Statement stat = getConnection().createStatement();
    }
}
