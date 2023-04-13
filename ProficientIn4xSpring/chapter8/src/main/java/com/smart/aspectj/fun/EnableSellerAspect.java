package com.smart.aspectj.fun;

import com.smart.Seller;
import com.smart.SmartSeller;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.DeclareParents;

@Aspect
public class EnableSellerAspect {
    @DeclareParents(value = "com.smart.NaiveWaiter", defaultImpl = SmartSeller.class)
    public static Seller seller;
}
