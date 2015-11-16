This is a simple example to create a producer (producer.py) and a consumer (consumer.py) to stream Avro via Kafka

Install packets via PIP
```
pip install -r requirements.txt
```

Run consumer:
```
python  consumer.py
```

Run producer:
```
python producer.py
```

Please make sure that you had [Kafka in your machine](https://sonnguyen.ws/install-apache-kafka-in-ubuntu-14-04/). And please correct the connection information before running.

In the source code repository above, I also created consumer_bottledwater-pg.py to decode avro data that pushed from bottedwater-pg Kafka producer.

