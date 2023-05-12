package com.smart.anno;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;

@Component
public class MyComponent {
    // Spring 会将窗口中所有类型为 Plugin 的 Bean 注入这个变量中
    @Autowired(required = false)
    private List<Plugin> plugins;

    // 钭 Plugin 类型的 Bean 注入 Map 中
    @Autowired
    private Map<String, Plugin> pluginMaps;

    public List<Plugin> getPlugins() {
        return plugins;
    }
}
