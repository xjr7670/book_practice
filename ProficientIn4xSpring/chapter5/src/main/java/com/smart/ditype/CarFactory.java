package com.smart.ditype;

public class CarFactory {
    // 创建 Car 的工厂方法
    public static Car createHongQiCar() {
        Car car = new Car();
        car.setBrand("红旗CA72");
        return car;
    }
}
