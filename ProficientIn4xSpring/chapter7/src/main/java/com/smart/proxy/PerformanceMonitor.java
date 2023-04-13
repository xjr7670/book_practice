package com.smart.proxy;

public class PerformanceMonitor {
    // 通过一个 ThreadLocal 保存与调用线程相关的性能监视信息
    private static ThreadLocal<MethodPerformance> performanceRecord = new ThreadLocal<MethodPerformance>();

    // 2 启动对某一目标方法的性能监视
    public static void begin(String method) {
        System.out.println("begin minitor...");
        MethodPerformance mp = new MethodPerformance(method);
        performanceRecord.set(mp);
    }
    public static void end() {
        System.out.println("end monitor...");
        MethodPerformance mp = performanceRecord.get();

        // 3 打印出方法性能监视的结果信息
        mp.printPerformance();
    }
}
