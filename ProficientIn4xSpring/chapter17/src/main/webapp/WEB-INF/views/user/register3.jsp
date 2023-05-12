<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
<head>
    <title>注册用户</title>
    <style type="text/css">
        .errorClass {
            color: red;
        }
    </style>
</head>
<body>
    <form:form modelAttribute="user" action="/chapter17/user/handle91.html">
        <form:errors path="*" />
        <table>
            <tr>
                <td>用户名：</td>
                <td>
                    <form:errors path="userName" cssClass="errorClass" />
                    <form:input path="userName" />
                </td>
            </tr>
            <tr>
                <td>密码：</td>
                <td>
                    <form:errors path="password" cssClass="errorClass" />
                    <form:password path="password" />
                </td>
            </tr>
            <tr>
                <td colspan="2"><input type="submit" name="提交"></td>
            </tr>
        </table>
    </form:form>
</body>
</html>