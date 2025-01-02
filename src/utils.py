import pika
import os
from loguru import logger

MQ_HOST = os.getenv('MQ_HOST', '')
MQ_PORT = os.getenv('MQ_PORT', 5672)
MQ_USER = os.getenv('MQ_USER', '')
MQ_PASSWORD = os.getenv('MQ_PASSWORD', '')
MQ_QUEUE = os.getenv('MQ_QUEUE', 'test_queue')


class QueueCommunication:
    def __init__(self, host: str, port: str, queue_name: str):
        self.host = host
        self.port = port
        self.queue_name = queue_name

    def connect(self, username: str, password: str):
        credentials = pika.PlainCredentials(username, password)
        connection_params = pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            virtual_host='/',
            credentials=credentials,
        )
        self.connection = pika.BlockingConnection(connection_params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)

    def produce(self, message: str):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message,
        )
        logger.info(f'=> Sent {message}')

    def start_consume(self, callback):
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=callback,
            auto_ack=True,
        )
        self.channel.start_consuming()
