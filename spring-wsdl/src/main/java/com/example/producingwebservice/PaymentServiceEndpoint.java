package com.example.producingwebservice;

import io.spring.guides.gs_producing_web_service.TransactionRequest;
import io.spring.guides.gs_producing_web_service.TransactionResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

/**
 * @author Sachin Sharma
 */

@Endpoint
public class PaymentServiceEndpoint {

    private static final String NAMESPACE_URI = "http://spring.io/guides/gs-producing-web-service";

    private PaymentService paymentService;

    @Autowired
    public PaymentServiceEndpoint(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "transactionRequest")
    @ResponsePayload
    public TransactionResponse getPaymentStatus(@RequestPayload TransactionRequest request) {
        TransactionResponse response = new TransactionResponse();
        response.setPaymentStatus(paymentService.getPaymentStatus(request.getName()));
        return response;
    }
}
