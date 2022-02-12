# Local kafka setup
Local Kafka setup with zookeeper for testing purposes

### Requirements
- python 3
- docker
- docker-compose

### Technology
- python 3
- Kafka
- Zookeeper


### Setup
##### create virtual environment
```
python -m venv venv
```

##### Install required packages
```
pip install -r requirements.txt
```

##### Running consumers
```
python consumer.py
```
```
python consumer-2.py
```


##### Running Producers
```
python producer.py
```