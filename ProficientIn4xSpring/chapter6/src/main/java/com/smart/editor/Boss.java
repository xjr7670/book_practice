package com.smart.editor;

public class Boss {
    private String name;
    private Car car = new Car();

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }
}
