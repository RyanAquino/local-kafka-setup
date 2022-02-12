from kafka import KafkaProducer

TOPIC_NAME = "items"
KAFKA_SERVER = "localhost:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

producer.send(TOPIC_NAME, b"test message", partition=0)
producer.flush()
