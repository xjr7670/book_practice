package com.smart.service;

import org.springframework.context.ApplicationContext;
import org.unitils.UnitilsTestNG;
import org.unitils.spring.annotation.SpringApplicationContext;

@SpringApplicationContext({"smart-service.xml", "smart-dao.xml"})
public class BaseServiceTest extends UnitilsTestNG {

    // 加载 spring 应用上下文
    @SpringApplicationContext
    public ApplicationContext applicationContext;
}
