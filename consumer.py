from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

import os

# Read environment variables
strKafkaHost = os.environ['KAFKA_SERVICE_HOST']
strKafkaPort = os.environ['KAFKA_SERVICE_PORT']
strTopicName = os.environ['KAFKA_TOPIC']

strMongoHost = os.environ['MONGO_SERVICE_HOST']
strMongoPort = os.environ['MONGO_SERVICE_PORT']

strMongoUser = os.environ['MONGO_USERNAME']
strMongoPswd = os.environ['MONGO_PASSWORD']

# Create connection to Kafka
consumer = KafkaConsumer(
		strTopicName,
		bootstrap_servers=[strKafkaHost + ':' + strKafkaPort],
		auto_offset_reset='earliest',
		enable_auto_commit=True,
		group_id='demo-group',
		value_deserializer=lambda x: loads(x.decode('utf-8')))

# Create connection to MongoDB
strConnectionString = 'mongodb://' + strMongoUser + ':' + strMongoPswd + '@' + strMongoHost + ':' + strMongoPort
db_conn = MongoClient(strConnectionString)

# Read messages from Kafka and put them into MongoDB
for message in consumer:
	message = message.value
	db_conn.demo.demo.insert_one(message)
	print(message)

