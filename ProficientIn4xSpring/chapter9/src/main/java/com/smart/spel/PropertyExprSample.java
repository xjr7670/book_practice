package com.smart.spel;

import com.smart.PlaceOfBirth;
import com.smart.User;
import org.springframework.expression.EvaluationContext;
import org.springframework.expression.ExpressionParser;
import org.springframework.expression.spel.standard.SpelExpressionParser;
import org.springframework.expression.spel.support.StandardEvaluationContext;

import java.util.Date;

public class PropertyExprSample {
    public static void main(String[] args) {
        // 1 构造一个对象
        User user = new User();
        user.setUserName("tom");
        user.setLastVisit(new Date());
        user.setCredits(100);
        user.setPlaceOfBirth(new PlaceOfBirth("中国", "厦门"));

        // 2 构造 SpEL 解析上下文
        ExpressionParser parser = new SpelExpressionParser();
        EvaluationContext context = new StandardEvaluationContext(user);

        // 3 基本属性值获取
        String username = (String) parser.parseExpression("userName").getValue(context);
        int credits = (Integer) parser.parseExpression("credits + 10").getValue(context);

        System.out.println(username);
        System.out.println(credits);

        // 4 嵌套对象属性值获取
        String city = (String) parser.parseExpression("placeOfBirth.city").getValue(context);
        System.out.println(city);
    }
}
