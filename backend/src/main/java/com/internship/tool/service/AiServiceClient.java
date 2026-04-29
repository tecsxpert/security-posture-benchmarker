package com.internship.tool.service;

import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.client.SimpleClientHttpRequestFactory;

import java.util.HashMap;
import java.util.Map;

@Service
public class AiServiceClient {

    private final RestTemplate restTemplate;
    private static final String AI_SERVICE_URL = "http://127.0.0.1:5000/analyze";

    public AiServiceClient() {
        this.restTemplate = new RestTemplate(getRequestFactory());
    }

    private SimpleClientHttpRequestFactory getRequestFactory() {
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        factory.setConnectTimeout(10000); // 10 sec
        factory.setReadTimeout(10000);    // 10 sec
        return factory;
    }

    public String analyze(String input) {
        try {
            // Request body
            Map<String, String> request = new HashMap<>();
            request.put("input", input);

            // Headers
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            HttpEntity<Map<String, String>> entity =
                    new HttpEntity<>(request, headers);

            // API call
            ResponseEntity<Map> response = restTemplate.exchange(
                    AI_SERVICE_URL,
                    HttpMethod.POST,
                    entity,
                    Map.class
            );

            // Handle response
            if (response.getStatusCode() == HttpStatus.OK && response.getBody() != null) {
                Object result = response.getBody().get("result");
                return result != null ? result.toString() : null;
            }

        } catch (Exception e) {
            System.out.println("AI Service Error: " + e.getMessage());
        }

        return null; // required
    }
}