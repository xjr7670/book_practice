package com.xjr7670;

import org.apache.log4j.Logger;
import org.junit.Test;

public class Log4jTest {

    @Test
    public void test() {
        final Logger logger = Logger.getLogger(Log4jTest.class);
        logger.info("hello this is log4j info log");
    }
}
