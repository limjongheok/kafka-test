from fastapi import FastAPI
from kafka_consumer import create_consumer, consume_messages
import threading

app = FastAPI()
consumer = create_consumer()
def consumer_thread():
    consume_messages(consumer, 'ai')

thread = threading.Thread(target=consumer_thread)
thread.start()

@app.get("/")
def read_root():
    return {"Hello": "World"}