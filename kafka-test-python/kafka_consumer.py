# kafka_consumer.py
from confluent_kafka import Consumer, KafkaException
from kafka_producer import create_producer, produce_message

producer = create_producer()
def create_consumer():
    return Consumer({
        'bootstrap.servers': '218.150.140.4:9092',
        'group.id': 'group2',
        'auto.offset.reset': 'earliest'
    })

def consume_messages(consumer, topic):
    consumer.subscribe([topic])
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            print(f"Received message: {msg.value().decode('utf-8')}")
            produce_message(producer, "success", "key", "success")
    finally:
        consumer.close()