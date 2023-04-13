package com.smart;

import com.smart.aspectj.anno.NeedTest;

public class NaughtyWaiter implements Waiter {
    @NeedTest
    public void greetTo(String clientName) {
        System.out.println("NaughtyWaiter: Greet to " + clientName + "...");
    }
    public void serveTo(String clientName) {
        System.out.println("NaughtyWaiter: Serving to " + clientName + "...");
    }
}
