package com.example.demo.kafka;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Service
@RequiredArgsConstructor
@Slf4j
public class KafkaConsumerService {

	@KafkaListener(topics = "success", groupId = "${spring.kafka.consumer.group}")
	public void listen(String s) {
		System.out.println(s);
	}

}
