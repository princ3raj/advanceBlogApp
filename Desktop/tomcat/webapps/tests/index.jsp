<!DOCTYPE html>
<%@page language="java" contentType="text/html"%>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <h1>Hellow world</h1>

    <%
String userAgent = request.getHeader("user-agent");
out.println("<br/>user-agent " + userAgent);
%>
    
</body>
</html>