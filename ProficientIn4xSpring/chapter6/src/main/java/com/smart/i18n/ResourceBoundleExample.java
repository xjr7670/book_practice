package com.smart.i18n;

import java.util.Locale;
import java.util.ResourceBundle;

public class ResourceBoundleExample {
    public static void main(String[] args) {
        ResourceBundle rb1 = ResourceBundle.getBundle("com/smart/i18n/resource", Locale.US);
        ResourceBundle rb2 = ResourceBundle.getBundle("com/smart/i18n/resource", Locale.CHINA);

        System.out.println("us: " + rb1.getString("greeting.common"));
        System.out.println("cn: " + rb2.getString("greeting.common"));
    }
}
