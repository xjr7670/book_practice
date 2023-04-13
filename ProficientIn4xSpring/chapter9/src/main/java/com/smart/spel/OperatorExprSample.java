package com.smart.spel;

import org.springframework.expression.ExpressionParser;
import org.springframework.expression.spel.standard.SpelExpressionParser;

public class OperatorExprSample {
    public static void main(String[] args) {
        ExpressionParser parser = new SpelExpressionParser();

        // 1 加法操作，运行结果等于1
        int two = parser.parseExpression("1 + 1").getValue(Integer.class);
        String testString = parser.parseExpression("\"test\" + ' ' + \"string\"").getValue(String.class);

        // 2 减法操作，运行结果等于4
        int four = parser.parseExpression("1 - - 3").getValue(Integer.class);

        // 减法操作，运行结果等于 -9000
        double d = parser.parseExpression("10000.00 - 1e4").getValue(Double.class);

        // 3 乘法操作，运行结果等于6
        int six = parser.parseExpression("-2 * -3").getValue(Integer.class);

        // 乘法操作，运行结果等于 24.0
        double twentyFour = parser.parseExpression("2.0 * 3e0 * 4").getValue(Double.class);

        // 4 除法操作，运行结果等于 -2
        int minusTwo = parser.parseExpression("6 / -3").getValue(Integer.class);

        // 除法操作，运行结果等于1.0
        double one = parser.parseExpression("8.0 / 4e0 / 2").getValue(Double.class);

        // 5 求余操作，运行结果等于 3
        int three = parser.parseExpression(" 7 % 4").getValue(Integer.class);

        // 求余操作，运行结果等于1
        one = parser.parseExpression(" 8  / 5 % 2").getValue(Integer.class);

        // 6 优先级运算，运行结果等于 -21
        int minusTwentyOne = parser.parseExpression("1 + 2 - 3 * 8").getValue(Integer.class);
    }
}
