package com.smart.oxm.domain.jaxb;

import java.util.ArrayList;
import java.util.List;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
        "userName",
        "password",
        "credits",
        "lastIp",
        "logs"
})
@XmlRootElement(name = "user")
public class User {

    @XmlElement(required = true)
    protected String userName;
    @XmlElement(required = true)
    protected String password;
    protected int credits;
    @XmlElement(required = true)
    protected String lastIp;
    @XmlElement(required = true)
    protected User.Logs logs;
    @XmlAttribute
    protected Integer userId;

    /**
     * Gets the value of the userName property.
     *
     * @return
     *     possible object is
     *     {@link String }
     *
     */
    public String getUserName() {
        return userName;
    }

    /**
     * Sets the value of the userName property.
     *
     * @param value
     *     allowed object is
     *     {@link String }
     *
     */
    public void setUserName(String value) {
        this.userName = value;
    }

    /**
     * Gets the value of the password property.
     *
     * @return
     *     possible object is
     *     {@link String }
     *
     */
    public String getPassword() {
        return password;
    }

    /**
     * Sets the value of the password property.
     *
     * @param value
     *     allowed object is
     *     {@link String }
     *
     */
    public void setPassword(String value) {
        this.password = value;
    }

    /**
     * Gets the value of the credits property.
     *
     */
    public int getCredits() {
        return credits;
    }

    /**
     * Sets the value of the credits property.
     *
     */
    public void setCredits(int value) {
        this.credits = value;
    }

    /**
     * Gets the value of the lastIp property.
     *
     * @return
     *     possible object is
     *     {@link String }
     *
     */
    public String getLastIp() {
        return lastIp;
    }

    /**
     * Sets the value of the lastIp property.
     *
     * @param value
     *     allowed object is
     *     {@link String }
     *
     */
    public void setLastIp(String value) {
        this.lastIp = value;
    }

    /**
     * Gets the value of the logs property.
     *
     * @return
     *     possible object is
     *     {@link User.Logs }
     *
     */
    public User.Logs getLogs() {
        return logs;
    }

    /**
     * Sets the value of the logs property.
     *
     * @param value
     *     allowed object is
     *     {@link User.Logs }
     *
     */
    public void setLogs(User.Logs value) {
        this.logs = value;
    }

    /**
     * Gets the value of the userId property.
     *
     * @return
     *     possible object is
     *     {@link Integer }
     *
     */
    public Integer getUserId() {
        return userId;
    }

    /**
     * Sets the value of the userId property.
     *
     * @param value
     *     allowed object is
     *     {@link Integer }
     *
     */
    public void setUserId(Integer value) {
        this.userId = value;
    }


    /**
     * <p>Java class for anonymous complex type.
     *
     * <p>The following schema fragment specifies the expected content contained within this class.
     *
     * <pre>
     * &lt;complexType>
     *   &lt;complexContent>
     *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
     *       &lt;sequence>
     *         &lt;element name="loginLog" type="{}LoginLog" maxOccurs="unbounded"/>
     *       &lt;/sequence>
     *     &lt;/restriction>
     *   &lt;/complexContent>
     * &lt;/complexType>
     * </pre>
     *
     *
     */
    @XmlAccessorType(XmlAccessType.FIELD)
    @XmlType(name = "", propOrder = {
            "loginLog"
    })
    public static class Logs {

        @XmlElement(required = true)
        protected List<LoginLog> loginLog;

        /**
         * Gets the value of the loginLog property.
         *
         * <p>
         * This accessor method returns a reference to the live list,
         * not a snapshot. Therefore any modification you make to the
         * returned list will be present inside the JAXB object.
         * This is why there is not a <CODE>set</CODE> method for the loginLog property.
         *
         * <p>
         * For example, to add a new item, do as follows:
         * <pre>
         *    getLoginLog().add(newItem);
         * </pre>
         *
         *
         * <p>
         * Objects of the following type(s) are allowed in the list
         * {@link LoginLog }
         *
         *
         */
        public List<LoginLog> getLoginLog() {
            if (loginLog == null) {
                loginLog = new ArrayList<LoginLog>();
            }
            return this.loginLog;
        }

    }

}
