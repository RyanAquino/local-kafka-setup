from kafka import KafkaConsumer, TopicPartition
import time

TOPIC_NAME = "items"
KAFKA_SERVER = "localhost:9092"

consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER, group_id='group-1')
consumer.assign([TopicPartition('items', 1)])

for message in consumer:
	# time.sleep(5)
	print(f"Message: {message}")
