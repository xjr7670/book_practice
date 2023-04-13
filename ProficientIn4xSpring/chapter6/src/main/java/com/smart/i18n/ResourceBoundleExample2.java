package com.smart.i18n;

import java.text.MessageFormat;
import java.util.GregorianCalendar;
import java.util.Locale;
import java.util.ResourceBundle;

public class ResourceBoundleExample2 {
    public static void main(String[] args) {
        ResourceBundle rb1 = ResourceBundle.getBundle("com/smart/i18n/fmt_resource", Locale.US);
        ResourceBundle rb2 = ResourceBundle.getBundle("com/smart/i18n/fmt_resource", Locale.CHINA);
        Object[] params = {"John", new GregorianCalendar().getTime()};

        String str1 = new MessageFormat(rb1.getString("greeting.common"), Locale.US).format(params);
        String str2 = new MessageFormat(rb2.getString("greeting.common"), Locale.CHINA).format(params);
        String str3 = new MessageFormat(rb2.getString("greeting.afternoon"), Locale.CHINA).format(params);

        System.out.println(str1);
        System.out.println(str2);
        System.out.println(str3);
    }
}
