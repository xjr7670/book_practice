package com.smart.oxm.xstream.json;

import com.smart.oxm.domain.LoginLog;
import com.smart.oxm.domain.User;
import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.HierarchicalStreamReader;
import com.thoughtworks.xstream.io.json.JettisonMappedXmlDriver;
import com.thoughtworks.xstream.io.json.JsonHierarchicalStreamDriver;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.charset.Charset;
import java.util.Date;

public class XStreamJSONSample {
    private static XStream xStream;
    public static User getUser() {
        LoginLog log1 = new LoginLog();
        log1.setIp("192.168.1.91");
        log1.setLoginDate(new Date());
        LoginLog log2 = new LoginLog();
        log2.setIp("192.168.1.92");
        log2.setLoginDate(new Date());
        User user = new User();
        user.setUserId(1);
        user.setUserName("xstream");
        user.addLoginLog(log1);
        user.addLoginLog(log2);
        return user;
    }

    // 连续的没有分隔的 JSON 串
    public static void toJsonByJettisonMappedXmlDriver() throws Exception {
        User user = getUser();
        FileOutputStream outputStream = new FileOutputStream("out/jettisonMappedSample.json");
        OutputStreamWriter writer = new OutputStreamWriter(outputStream, Charset.forName("UTF-8"));
        xStream = new XStream(new JettisonMappedXmlDriver());
        xStream.setMode(XStream.NO_REFERENCES);
        xStream.alias("user", User.class);
        xStream.toXML(user, writer);
    }

    // 格式化良好的 json 串
    public static void toJsonByJsonHierarchicalStreamDriver() throws Exception {
        User user = getUser();
        FileOutputStream outputStream = new FileOutputStream("out/JsonByJsonHierarchicalSample.json");
        OutputStreamWriter writer = new OutputStreamWriter(outputStream, Charset.forName("UTF-8"));
        xStream = new XStream(new JsonHierarchicalStreamDriver());
        xStream.alias("user", User.class);
        xStream.toXML(user, writer);
    }

    // 解析 json
    public static void parseJsonByJettisonMappedXmlDriver() throws Exception {
        FileInputStream inputStream = new FileInputStream("out/JsonByJsonHierarchicalSample.json");
        InputStreamReader inputStreamReader = new InputStreamReader(inputStream, Charset.forName("UTF-8"));
        xStream = new XStream(new JettisonMappedXmlDriver());
        xStream.alias("user", User.class);
        User user = (User) xStream.fromXML(inputStreamReader);
        System.out.println(user.getUserName());
    }

    public static void main(String[] args) throws Exception {
//        toJsonByJettisonMappedXmlDriver();
//        toJsonByJsonHierarchicalStreamDriver();
        parseJsonByJettisonMappedXmlDriver();
    }
}
