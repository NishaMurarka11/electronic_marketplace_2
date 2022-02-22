package com.example.producingwebservice;

import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * @author Sachin Sharma
 */

@Component
public class PaymentService {

    List<String> paymentStatus = new ArrayList<>();


    @PostConstruct
    public void initData() {
        paymentStatus.add("TRUE");
        paymentStatus.add("FALSE");
    }

    // Send true with 95% probability
    public String getPaymentStatus(String name){
        System.out.println("Buyer Name"+name);
        Random rand = new Random();
        int  upperbound = 100;
        int int_random = rand.nextInt(upperbound);
        return int_random<=95?paymentStatus.get(0):paymentStatus.get(1);
    }


}
