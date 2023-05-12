package com.smart.spel;

import com.smart.User;
import org.springframework.expression.EvaluationContext;
import org.springframework.expression.ExpressionParser;
import org.springframework.expression.spel.standard.SpelExpressionParser;
import org.springframework.expression.spel.support.StandardEvaluationContext;

public class MethodExprSample {
    public static void main(String[] args) {
        User user = new User();
        ExpressionParser parser = new SpelExpressionParser();
        EvaluationContext context = new StandardEvaluationContext(user);

        // 1 与操作，结果为 false
        boolean falseValue = parser.parseExpression("true && false").getValue(Boolean.class);

        String expression = "isVipMember('tom') and isVipMember('jony')";
        boolean trueValue = parser.parseExpression(expression).getValue(context, Boolean.class);

        // 2 或操作，结果为 true
        trueValue = parser.parseExpression("true or false").getValue(Boolean.class);

        // 3 取非操作，结果为 false
        falseValue = parser.parseExpression("!true").getValue(Boolean.class);
    }
}
