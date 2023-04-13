package com.smart.spel;

import com.smart.PlaceOfBirth;
import org.testng.annotations.Test;

public class PlaceOfBirthTest {
    @Test
    public void birth() {
        PlaceOfBirth placeOfBirth = new PlaceOfBirth("中国", "厦门");
        System.out.println(placeOfBirth.city);
    }
}
