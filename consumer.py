from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

import os

strKafkaHost = os.environ['KAFKA_SERVICE_SERVICE_HOST']
strKafkaPort = os.environ['KAFKA_SERVICE_SERVICE_PORT']
strTopicName = os.environ['KAFKA_TOPIC']

strMongoHost = os.environ['MONGO_SERVICE_HOST']
strMongoPort = os.environ['MONGO_SERVICE_PORT']

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))