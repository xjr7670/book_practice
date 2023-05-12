package com.smart.ditype;

public class Boss {
    private String name;
    private Car car;
    private Office office;

    public Boss() {}
    public Boss(String name, Car car, Office office) {
        this.name = name;
        this.car = car;
        this.office = office;
    }

    public void setOffice(Office office) {
        this.office = office;
    }

    public void setCar(Car car) {
        this.car = car;
    }

    public void setName(String name) {
        this.name = name;
    }
}
