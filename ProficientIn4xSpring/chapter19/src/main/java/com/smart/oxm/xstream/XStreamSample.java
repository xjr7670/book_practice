package com.smart.oxm.xstream;

import com.smart.oxm.domain.LoginLog;
import com.smart.oxm.domain.User;
import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.Date;

public class XStreamSample {
    private static XStream xStream;

    static {
        xStream = new XStream(new DomDriver());
    }

    // 初始化转换对象
    public static User getUser() {
        LoginLog log1 = new LoginLog();
        log1.setIp("192.168.1.91");
        log1.setLoginDate(new Date());
        User user = new User();
        user.setUserId(1);
        user.setUserName("xstream");
        user.addLoginLog(log1);
        return user;
    }

    // java 对象转换为 XML
    public static void objectToXML() throws Exception {
        // 2-1 获取转换的 User 对象实例
        User user = getUser();

        // 2-2 实例化一个文件输出流
        FileOutputStream outputStream = new FileOutputStream("out/XStreamSample.xml");
        // 2-3 将 User 对象转换为 XML，并保存到指定文件
        xStream.toXML(user, outputStream);
    }

    // 3 xml 转换为 java 对象
    public static void XMLToObject() throws Exception {
        // 3-1 实例化一个文件输入流
        FileInputStream inputStream = new FileInputStream("out/XStreamSample.xml");

        // 3-2 将 XML 文件输入流转换为对象
        User user = (User) xStream.fromXML(inputStream);

        for (LoginLog log: user.getLogs()) {
            if (log != null) {
                System.out.println("访问IP：" + log.getIp());
                System.out.println("访问时间：" + log.getLoginDate());
            }
        }
    }

    public static void main(String[] args) throws Exception {
        XStreamSample.XMLToObject();
    }
}
