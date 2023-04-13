package com.smart.web;

import com.smart.domain.User;

import javax.servlet.http.HttpServletRequest;

public class BaseController {
    protected static final String ERROR_MSG_KEY = "errorMsg";

    protected User getSessionUser(HttpServletRequest request) {
        return (User) request.getSession().getAttribute(CommonConstant.USER_CONTEXT);
    }
}
