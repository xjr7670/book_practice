package com.smart.oxm.domain.jaxb;

import javax.xml.bind.annotation.adapters.XmlAdapter;
import java.util.Calendar;

public class Adapter1
        extends XmlAdapter<String, Calendar>
{


    public Calendar unmarshal(String value) {
        return (javax.xml.bind.DatatypeConverter.parseDate(value));
    }

    public String marshal(Calendar value) {
        if (value == null) {
            return null;
        }
        return (javax.xml.bind.DatatypeConverter.printDate(value));
    }

}
