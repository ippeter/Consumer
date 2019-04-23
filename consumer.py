from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

import os

strKafkaHost = os.environ['KAFKA_SERVICE_SERVICE_HOST']
strKafkaPort = os.environ['KAFKA_SERVICE_SERVICE_PORT']
strTopicName = os.environ['KAFKA_TOPIC']

strMongoHost = os.environ['MONGO_SERVICE_HOST']
strMongoPort = os.environ['MONGO_SERVICE_PORT']

strMongoUser = os.environ['MONGO_USERNAME']
strMongoPswd = os.environ['MONGO_PASSWORD']

consumer = KafkaConsumer(
		strTopicName,
		bootstrap_servers=[strKafkaHost + ':' + strKafkaPort],
		auto_offset_reset='earliest',
		enable_auto_commit=True,
		group_id='demo-group',
		value_deserializer=lambda x: loads(x.decode('utf-8')))

#
# DEBUG
#
strConnectionString = 'mongodb://' + strMongoUser + ':' + strMongoPswd + '@' + strMongoHost + ':' + strMongoPort
print(strConnectionString)

db_conn = MongoClient(strConnectionString)

for message in consumer:
	message = message.value
	db_conn.demo.demo.insert_one(message)
	print(message)

