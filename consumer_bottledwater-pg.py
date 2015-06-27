"""
Sat Jun 27, 2015 12:30:32 added by Thanh Son 
Email: thanhson1085@gmail.com 

This script is a simple example to decode data from bottledwater-pg -> kafka
"""
from kafka import KafkaConsumer
import avro.schema
import avro.io
import io

# To consume messages
consumer = KafkaConsumer('test2',
                         group_id='',
                         bootstrap_servers=['kafka:9092'])


schema = """
{
    "namespace":"com.martinkl.bottledwater.dbschema.public",
    "type":"record",
    "name":"test",
    "fields":[
        {"name":"id","type":["null", "int"]},
        {"name":"value","type":["null", "string"]}
    ]
}
"""
schema = avro.schema.parse(schema)
for msg in consumer:
    value = bytearray(msg.value)
    bytes_reader = io.BytesIO(value[5:]) # remove 5-byte header, the first byte is reserved for future, 4 bytes for 32 bit number indicating ID
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(schema)
    hello = reader.read(decoder)
    print hello
