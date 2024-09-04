from confluent_kafka import Producer

def create_producer():
    return Producer({'bootstrap.servers': '218.150.140.4:9092'})

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")
        
def produce_message(producer, topic, key, value):
    producer.produce(topic, key=key, value=value, callback=delivery_report)
    producer.flush()