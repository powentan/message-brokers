from utils import QueueCommunication, MQ_HOST, MQ_PORT, MQ_USER, MQ_PASSWORD, MQ_QUEUE
from loguru import logger

def consumer_callback(channel, method, properties, body):
    logger.info(f'<= Received {body}')

mq = QueueCommunication(host=MQ_HOST, port=MQ_PORT, queue_name=MQ_QUEUE)

try:
    mq.connect(MQ_USER, MQ_PASSWORD)
except Exception as e:
    logger.error(f'error: {e}')

mq.start_consume(callback=consumer_callback)
