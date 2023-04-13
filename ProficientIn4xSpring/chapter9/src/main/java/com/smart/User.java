package com.smart;

import java.util.*;

public class User {
    private String userName;
    private int credits;
    private Date lastVisit;
    private PlaceOfBirth placeOfBirth;
    public String[] interestsArray = {"John", "Tom", "Cavin", "Dom"};
    public List<String> interestsList = new ArrayList<>();
    public Map<String, String> interestsMap = new HashMap<>();

    public void setInterestsList(List<String> interestsList) {
        this.interestsList = interestsList;
    }

    public User() {
        interestsList.add("Yesterday once more");
        interestsList.add("far away from home");
        interestsMap.put("interest1", "hello");
    }

    public User(String userName) {
        this.userName = userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }
    public String getUserName() {
        return this.userName;
    }

    public void setCredits(int credits) {
        this.credits = credits;
    }
    public int getCredits() {
        return this.credits;
    }

    public void setLastVisit(Date lastVisit) {
        this.lastVisit = lastVisit;
    }
    public Date getLastVisit() {
        return this.lastVisit;
    }

    public void setPlaceOfBirth(PlaceOfBirth placeOfBirth) {
        this.placeOfBirth = placeOfBirth;
    }
    public PlaceOfBirth getPlaceOfBirth() {
        return this.placeOfBirth;
    }

    public boolean isVipMember(String userName) {
        return "tom".equals(userName);
    }

    // 实例方法
    public boolean validatePassword(String password) {
        return password.length() > 8;
    }

    // 私有方法
    private boolean validatePassword2(String password) {
        return password.length() > 8;
    }

    // 静态方法
    public static boolean validatePassword3(String password) {
        return password.length() > 8;
    }

    // 对象方法
    public void addInterests(String... arg) {
        for (int i = 0; i < arg.length; i++) {
            this.interestsList.add(arg[i]);
            System.out.println(arg[i] + " has been added to interestsList.");
        }
    }
}
