package com.smart.web;

import com.smart.domain.User;
import org.springframework.mock.web.MockHttpServletRequest;
import org.springframework.mock.web.MockHttpServletResponse;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.unitils.UnitilsTestNG;
import org.unitils.spring.annotation.SpringApplicationContext;
import org.unitils.spring.annotation.SpringBeanByName;
import org.unitils.spring.annotation.SpringBeanByType;

import static org.hamcrest.Matchers.*;
import static org.junit.Assert.assertThat;
import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotNull;

@SpringApplicationContext({"classpath:applicationContext.xml", "/web/smart-servlet.xml"})
public class LoginControllerTest extends UnitilsTestNG {
    @SpringBeanByType
    private RequestMappingHandlerAdapter handlerAdapter;

    @SpringBeanByType
    private LoginController controller;

    private MockHttpServletRequest request;
    private MockHttpServletResponse response;

    @BeforeClass
    public void before() {
        request = new MockHttpServletRequest();
        request.setCharacterEncoding("UTF-8");
        response = new MockHttpServletResponse();
    }

    @SpringBeanByType
    private RestTemplate restTemplate;

    @Test
    public void loginCheck() throws  Exception {
        request.setRequestURI("/loginCheck.html");
        request.addParameter("userName", "tom");
        request.addParameter("password", "123456");

        ModelAndView mav = controller.loginCheck(request);
        User user = (User) request.getSession().getAttribute("user");

        assertNotNull(mav);
        assertEquals(mav.getViewName(), "main");
        assertNotNull(user);
        assertThat(user.getUserName(), equalTo("tom"));
        assertThat(user.getCredit(), greaterThan(5));

        MultiValueMap<String, String> map = new LinkedMultiValueMap<>();
        map.add("userName", "tom");
        map.add("password", "123456");

        String result = restTemplate.postForObject("http://localhost:8000/bbs/loginCheck.html", map, String.class);

        assertNotNull(result);
        assertThat(result, containsString("tom,欢迎您进入小春论坛"));

    }


}
