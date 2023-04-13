<html>
<head>
    <title>smart</title>
</head>
<body>
    用户列表
    <table>
        <#list userList as user>
        <tr>
            <td>
                <a href="/user/showUser/${user.userName}.html">${user.userName}</a>
            </td>
            <td>${user.realName}</td>
            <td>${user.birthday?string("yyyy-MM-dd")}</td>
        </tr>
        </#list>
    </table>
</body>
</html>