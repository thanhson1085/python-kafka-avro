import io
import avro.schema
import avro.io
from kafka import KafkaConsumer

# To consume messages
CONSUMER = KafkaConsumer('my-topic',
                         group_id='my_group',
                         bootstrap_servers=['localhost:9092'])

SCHEMA_PATH = "user.avsc"
SCHEMA = avro.schema.parse(open(SCHEMA_PATH).read())

for msg in CONSUMER:
    bytes_reader = io.BytesIO(msg.value)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(SCHEMA)
    user1 = reader.read(decoder)
    print user1
