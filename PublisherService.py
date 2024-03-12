
'''Referanc:
For MongoDb==>https://www.youtube.com/watch?v=rvXhj-FyzcE
For RabbitMq===>https://www.rabbitmq.com/tutorials.


'''
import json
import logging
import pymongo
import pika
from SenderService import *


MONGODB_URI = "mongodb://localhost:27017/"
DB_NAME = "iot_data"
COLLECTION_NAME = "messages"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MessageProcessor:
    def __init__(self, mongodb_uri, db_name, collection_name, rabbitmq_host, rabbitmq_port, rabbitmq_queue):
        self.mongodb_uri = mongodb_uri
        self.db_name = db_name
        self.collection_name = collection_name
        self.rabbitmq_host = rabbitmq_host
        self.rabbitmq_port = rabbitmq_port
        self.rabbitmq_queue = rabbitmq_queue
        self.mongo_client = pymongo.MongoClient(self.mongodb_uri)
        self.db = self.mongo_client[self.db_name]
        self.collection = self.db[self.collection_name]

    def process_message(self, message):
        try:
            logger.info(f"Received message: {message}")
            self.collection.insert_one(message)
            logger.info("Message inserted into MongoDB")
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            
            
            
    def on_message(self, channel, method, properties, body):
        try:
            payload = json.loads(body.decode("utf-8"))
            self.process_message(payload)
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")





    def connect_rabbitmq(self):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(self.rabbitmq_host, self.rabbitmq_port))
            channel = connection.channel()
            channel.queue_declare(queue=self.rabbitmq_queue)
            channel.basic_consume(queue=self.rabbitmq_queue, on_message_callback=self.on_message, auto_ack=True)
            logger.info("Connected to RabbitMQ and subscribed to queue")
            channel.start_consuming()
        except Exception as e:
            logger.error(f"Error connecting to RabbitMQ: {e}")


def main():
    
    processor = MessageProcessor(MONGODB_URI, DB_NAME, COLLECTION_NAME, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_QUEUE)
    processor.connect_rabbitmq()

if __name__ == "__main__":
    main()
