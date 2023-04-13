package com.smart.oxm.domain.jaxb;

import java.util.Calendar;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlType;
import javax.xml.bind.annotation.adapters.XmlJavaTypeAdapter;


@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "LoginLog", propOrder = {
        "userId",
        "ip",
        "loginDate"
})
public class LoginLog {

    @XmlElement(required = true)
    protected String userId;
    @XmlElement(required = true)
    protected String ip;
    @XmlElement(required = true, type = String.class)
    @XmlJavaTypeAdapter(Adapter1 .class)
    protected Calendar loginDate;
    @XmlAttribute
    protected Integer loginLogId;


    public String getUserId() {
        return userId;
    }


    public void setUserId(String value) {
        this.userId = value;
    }


    public String getIp() {
        return ip;
    }


    public void setIp(String value) {
        this.ip = value;
    }


    public Calendar getLoginDate() {
        return loginDate;
    }


    public void setLoginDate(Calendar value) {
        this.loginDate = value;
    }


    public Integer getLoginLogId() {
        return loginLogId;
    }


    public void setLoginLogId(Integer value) {
        this.loginLogId = value;
    }

}
