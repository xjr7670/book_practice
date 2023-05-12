<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <title>websocket测试</title>
    <script type="text/javascript">
        var url = "ws://" + window.location.host + '<%=request.getContextPath()%>/hello';
        var sock = new Websocket(url);  // 打开  websocket
        sock.onopen = function() {
            console.log('开启websocket连接！');
            sayHello();
        }

        sock.onmessage = function(e) {
            console.log('接收消息：', e.data);
            setTimeout(function() { sayHello() }, 2000);
        }

        sock.onclose = function() {
            console.log('关闭 websocket 连接！');
        }

        function sayHello() {
            console.log('发送消息: hello world!');
            sock.send('hello world!');
        }
    </script>
</head>
<body>
    hello world!
</body>
</html>