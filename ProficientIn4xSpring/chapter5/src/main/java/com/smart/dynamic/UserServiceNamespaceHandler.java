package com.smart.dynamic;

import org.springframework.beans.factory.xml.NamespaceHandlerSupport;

public class UserServiceNamespaceHandler extends NamespaceHandlerSupport {
    public void init() {
        registerBeanDefinitionParser("user-service", new UserServiceDefinitionParser());
    }
}
