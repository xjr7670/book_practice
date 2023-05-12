package com.smart.spel;

import org.springframework.expression.ExpressionParser;
import org.springframework.expression.spel.standard.SpelExpressionParser;

public class LiteralExprSample {
    public static void main(String[] args) {
        ExpressionParser parser = new SpelExpressionParser();

        // 1 解析字符串
        String helloWorld = (String) parser.parseExpression("\"Hello World\"").getValue();
        System.out.println(helloWorld);

        // 2 解析双精度浮点型
        double doubleNumber = (Double) parser.parseExpression("6.0221415E+23").getValue();
        System.out.println(doubleNumber);

        // 3 解析整型
        int maxValue = (Integer) parser.parseExpression("0x7FFFFFFF").getValue();
        System.out.println(maxValue);

        // 4 解析整型布尔型
        boolean trueValue = (Boolean) parser.parseExpression("true").getValue();
        System.out.println(trueValue);

        // 5 解析空值
        Object nullValue = parser.parseExpression("null").getValue();
        System.out.println(nullValue);
    }
}
