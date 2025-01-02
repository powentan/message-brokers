import random
import time
from loguru import logger
from utils import QueueCommunication, MQ_HOST, MQ_PORT, MQ_USER, MQ_PASSWORD, MQ_QUEUE


mq = QueueCommunication(host=MQ_HOST, port=MQ_PORT, queue_name=MQ_QUEUE)
try:
    mq.connect(MQ_USER, MQ_PASSWORD)
except Exception as e:
    logger.error(f'error: {e}')

while True:
    delay = random.randint(0, 3)
    time.sleep(delay)
    mq.produce('Hello, World!')
