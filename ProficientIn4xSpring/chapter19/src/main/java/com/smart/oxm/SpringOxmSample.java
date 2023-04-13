package com.smart.oxm;

import com.smart.oxm.domain.jaxb.LoginLog;
import com.smart.oxm.domain.jaxb.User;
import org.springframework.oxm.Marshaller;
import org.springframework.oxm.Unmarshaller;

import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.GregorianCalendar;

public class SpringOxmSample {
    private Marshaller marshaller;
    private Unmarshaller unmarshaller;

    public static User getUser(){
        LoginLog log1 = new LoginLog();
        log1.setIp("192.168.1.91");
        log1.setLoginDate(new GregorianCalendar());
        LoginLog log2 = new LoginLog();
        log2.setIp("192.168.1.92");
        log2.setLoginDate(new GregorianCalendar());
        LoginLog log3 = new LoginLog();
        log3.setIp("192.168.1.93");
        log3.setLoginDate(new GregorianCalendar());
        User user = new User();
        user.setUserName("jaxb");
        User.Logs logs = new User.Logs();
        logs.getLoginLog().add(log1);
        logs.getLoginLog().add(log2);
        logs.getLoginLog().add(log3);
        user.setLogs(logs);
        return user;
    }

    public void ObjectToXML() throws Exception {
        User user = getUser();
        FileOutputStream os = null;
        try {
            os = new FileOutputStream("out/SpringOxmSample.xml");
            this.marshaller.marshal(user, new StreamResult(os));
        } finally {
            //todo..
        }
    }

    public void XmlToObject() throws Exception {
        FileInputStream is = null;
        User user = null;
        try {
            is = new FileInputStream("out/SpringOxmSample.xml");
            user = (User) this.unmarshaller.unmarshal(new StreamSource((is)));
        } finally {
            //todo..
        }
    }

    public static void main(String[] args) throws Exception {
        SpringOxmSample springOxmSample = new SpringOxmSample();
        springOxmSample.ObjectToXML();
    }
}
