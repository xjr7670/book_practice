package com.smart;

public class SmartSeller implements Seller {
    public void sell(String goods, String clientName) {
        System.out.println("sell " + goods + " to " + clientName);
    }
    protected int showGoods(String goods) {
        System.out.println("show goods of " + goods + "...");
        return 1;
    }
    public void checkBill(int billId) {
        if (billId == 1) {
            throw new IllegalArgumentException("iae Exception");
        } else {
            throw new RuntimeException("re Exception");
        }
    }
}
