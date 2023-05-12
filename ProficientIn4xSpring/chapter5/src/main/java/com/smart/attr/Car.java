package com.smart.attr;

public class Car {
    private int maxSpeed;
    private String brand;
    private String corp;
    private double price;

    public void setBrand(String brand) {
        this.brand = brand;
    }
    public void setMaxSpeed(int maxSpeed) {
        this.maxSpeed = maxSpeed;
    }
    public void setPrice(double price) {
        this.price = price;
    }
    public void setCorp(String corp) {
        this.corp = corp;
    }

    public Car() {}
    public Car(String brand, double price) {
        this.brand = brand;
        this.price = price;
    }
    public Car(String brand, String corp, double price) {
        this.brand = brand;
        this.corp = corp;
        this.price = price;
    }
    public Car(String brand, String corp, int maxSpeed) {
        this.brand = brand;
        this.corp = corp;
        this.maxSpeed = maxSpeed;
    }

    public String toString() {
        return "brand: " + this.brand + "/maxSpeed: " + this.maxSpeed + "/price: " + this.price;
    }
}

