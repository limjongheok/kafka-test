package com.example.demo;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.kafka.KafkaProducerService;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@RestController
@RequiredArgsConstructor
@Slf4j
public class Controller {

	private final KafkaProducerService kafkaProducerService;

	@GetMapping("/api")
	public ResponseEntity<?> ok() {
		kafkaProducerService.sendMessage("전송");
		return ResponseEntity.ok().body("전송");
	}
}
