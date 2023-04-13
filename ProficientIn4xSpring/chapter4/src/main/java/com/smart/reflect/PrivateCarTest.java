package com.smart.reflect;

import sun.awt.windows.ThemeReader;

import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class PrivateCarTest {
    public static void main(String[] args) throws Throwable {
        ClassLoader loader = Thread.currentThread().getContextClassLoader();
        Class clazz = loader.loadClass("com.smart.reflect.PrivateCar");
        PrivateCar pcar = (PrivateCar) clazz.newInstance();
        Field colorFld = clazz.getDeclaredField("color");

        // 取消 java 语言访问检查以访问 private 变量
        colorFld.setAccessible(true);
        colorFld.set(pcar, "红色");

        Method driveMtd = clazz.getDeclaredMethod("drive", (Class[])null);
        // 取消 java 访问访问检查以访问 protected 方法
        driveMtd.setAccessible(true);
        driveMtd.invoke(pcar, (Object[]) null);
    }
}
