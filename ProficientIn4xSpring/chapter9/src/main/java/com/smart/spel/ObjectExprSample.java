package com.smart.spel;

import com.smart.User;
import org.springframework.expression.EvaluationContext;
import org.springframework.expression.ExpressionParser;
import org.springframework.expression.spel.standard.SpelExpressionParser;
import org.springframework.expression.spel.support.StandardEvaluationContext;

import java.lang.reflect.Array;
import java.util.*;

public class ObjectExprSample {
    public static void main(String[] args) {
        User user = new User();
        user.setUserName("tom");

        ExpressionParser parser = new SpelExpressionParser();
        StandardEvaluationContext context = new StandardEvaluationContext(user);

        // 1 通过setValue赋值
        parser.parseExpression("userName").setValue(context, "jony");
        System.out.println(user.getUserName());

        // 2 通过表达式赋值
        parser.parseExpression("userName='anyli'").getValue(context);
        System.out.println(user.getUserName());

        // 3 加载 java.lang.string
        Class stringClass = parser.parseExpression("T(java.lang.String)").getValue(Class.class);
        System.out.println(stringClass==java.lang.String.class);

        // 4 加载 com.smart.User
        Class userClass = parser.parseExpression("T(com.smart.User)").getValue(Class.class);
        System.out.println(userClass == com.smart.User.class);

        // 5 调用静态类方法
        Object randomValue = parser.parseExpression("T(java.lang.Math).random()").getValue();
        System.out.println(randomValue);

        // 6 使用构造器
        user = parser.parseExpression("new com.smart.User('tom')").getValue(User.class);
        System.out.println(user.getUserName());

        // 7 变量解析
        // 7-1 为 newUserName 变量设置新值
        EvaluationContext context1 = new StandardEvaluationContext(user);
        context1.setVariable("newUserName", "jony");

        // 7-2 取变量值，并赋值
        parser.parseExpression("userName=#newUserName").getValue(context1);
        System.out.println(user.getUserName());

        // 7-3 this 变量值使用
        List<Integer> credits = new ArrayList<Integer>();
        credits.addAll(Arrays.asList(150, 100, 90, 50, 110, 130, 70));
        context.setVariable("credits", credits);
        List<Integer> creditsGreater100 = (List<Integer>) parser.parseExpression("#credits.?[#this>100]").getValue(context);
        System.out.println(creditsGreater100.toString());

        // 8 集合过滤
        Map<String, Integer> creditsMap = new HashMap<>();
        creditsMap.put("Tom", 95);
        creditsMap.put("Jony", 110);
        creditsMap.put("Morin", 85);
        creditsMap.put("Mose", 120);
        creditsMap.put("Morrow", 60);
        context1.setVariable("credits", creditsMap);

        Map<String, Integer> creditsGreater100_1 = (Map<String, Integer>) parser.parseExpression("#credits.?[value>90]").getValue(context1);
        System.out.println(creditsGreater100_1.toString());

        // 9 集合转换
        List<Boolean> creditsGreater100_2 = (List<Boolean>) parser.parseExpression("#credits.![#this>100]").getValue(context);
        System.out.println(creditsGreater100_2.toString());
    }
}
