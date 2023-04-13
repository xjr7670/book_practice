package com.smart.spel;

import com.smart.PlaceOfBirth;
import com.smart.User;
import org.springframework.expression.EvaluationContext;
import org.springframework.expression.ExpressionParser;
import org.springframework.expression.spel.standard.SpelExpressionParser;
import org.springframework.expression.spel.support.StandardEvaluationContext;

import java.util.Date;
import java.util.List;
import java.util.Map;

public class CollectionExprExample {
    public static void main(String[] args) {
        User user = new User();
        user.setUserName("tom");
        user.setLastVisit(new Date());
        user.setCredits(100);
        user.setPlaceOfBirth(new PlaceOfBirth("中国", "厦门"));

        ExpressionParser parser = new SpelExpressionParser();
        EvaluationContext context = new StandardEvaluationContext(user);

        int[] array1 = (int[]) parser.parseExpression("new int[]{1, 2, 3}").getValue(context);
        int[][] array2 = (int[][]) parser.parseExpression("new int[2][3]").getValue(context);

        // 目前不支持多维数据初始化，以下语句将报错
        //int[][] array3 = (int[][]) parser.parseExpression("new int[2][3]{{1, 2, 3}, {4, 5, 6}}").getValue(context);

        // 2 List 表达式解析
        List list = (List) parser.parseExpression("{1,2,3,4}").getValue(context);
        List ListOfLists = (List) parser.parseExpression("{{'a', 'b'}, {'x', 'y'}}").getValue(context);

        // 3 列表字符串解析
        Map userInfo = (Map) parser.parseExpression("{userName: 'tom', credits: 100}").getValue(context);
        List userInfo2 = (List) parser.parseExpression("{{userName:'tom', credits:100}, {userName: 'tom', credits:100}}").getValue(context);

        // 4 从数组，List，Map 中取值
        String interest1 = (String) parser.parseExpression("interestsArray[0]").getValue(context);
        String interest2 = (String) parser.parseExpression("interestsList[0]").getValue(context);
        String interest3 = (String) parser.parseExpression("interestsMap['interest1']").getValue(context);

        System.out.println("array1: " + array1.toString());
        System.out.println("array2: " + array2.toString());
        System.out.println("list: " + list.toString());
        System.out.println("interest1: " + interest1);
        System.out.println("interest2: " + interest2);
        System.out.println("interest3: " + interest3);
    }
}
