package com.smart.resource;

import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.core.io.support.ResourcePatternResolver;
import org.testng.annotations.Test;

import static org.testng.Assert.assertNotNull;

public class PatternResolverTest {
    @Test
    public void getResource() throws Throwable {
        ResourcePatternResolver resolver = new PathMatchingResourcePatternResolver();

        // 加载所有类包 com.smart 及子孙包下以 .xml 为后缀的资源
        Resource resources[] = resolver.getResources("classpath*:com/smart/**/*.xml");
        assertNotNull(resources);
        for (Resource resource:resources) {
            System.out.println(resource.getDescription());
        }
    }
}
