import io
import random
import avro.schema
from avro.io import DatumWriter
from kafka import SimpleProducer
from kafka import KafkaClient

# To send messages synchronously
KAFKA = KafkaClient('localhost:9092')
PRODUCER = SimpleProducer(KAFKA)

# Kafka topic
TOPIC = "my-topic"

# Path to user.avsc avro schema
SCHEMA_PATH = "user.avsc"
SCHEMA = avro.schema.parse(open(SCHEMA_PATH).read())

for i in xrange(10):
    writer = DatumWriter(SCHEMA)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write({"name": "123", "favorite_color": "111", "favorite_number": random.randint(0, 10)}, encoder)
    raw_bytes = bytes_writer.getvalue()
    PRODUCER.send_messages(TOPIC, raw_bytes)
