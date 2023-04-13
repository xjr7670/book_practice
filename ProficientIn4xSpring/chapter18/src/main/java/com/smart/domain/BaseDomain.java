package com.smart.domain;

import java.io.Serializable;
import org.apache.commons.lang.builder.ToStringBuilder;

public class BaseDomain implements Serializable {
    public String toString() {
        return ToStringBuilder.reflectionToString(this);
    }
}
