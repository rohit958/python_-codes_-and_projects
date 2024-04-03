import time
from kafka import KafkaProducer

TOPIC_NAME = "test-topic"

producer = KafkaProducer(
    bootstrap_servers=f"kafka-10ef12ea-demo-rohitkushwaha630-8673.a.aivencloud.com:22932",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

for i in range(100):
    message = f"Hello from Python using SSL {i + 1}!"
    producer.send(TOPIC_NAME, message.encode('utf-8'))
    print(f"Message sent: {message}")
    time.sleep(1)

#producer.close()