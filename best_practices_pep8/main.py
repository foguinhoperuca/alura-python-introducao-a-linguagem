from typing import Any
import logging

from util import LOG_FORMAT_INFO
from queue import QueueFactory, QueueType, TypeBaseQueue
from stats import ResumedStats, DetailedStats


logging.basicConfig(level=logging.INFO, format=LOG_FORMAT_INFO)

logging.info('--- Normal Queue: ---')

nq: TypeBaseQueue = QueueFactory.fabricate(QueueType.NORMAL_QUEUE)
nq.update_queue()
nq.update_queue()
nq.update_queue()
print(nq.call_client(5))
print(nq.call_client(10))

print("++++++++++++++++++++++++++++++++++++++++++++")
logging.info('Priority Queue:')

manufactured: Any = QueueFactory.fabricate(QueueType.PRIORITY_QUEUE)
manufactured.update_queue()
manufactured.update_queue()
manufactured.update_queue()
manufactured.update_queue()
print(manufactured.call_client(10))
print(manufactured.call_client(20))
print(manufactured.call_client(30))
print(manufactured.statistics(ResumedStats(day='1993-01-10', agency=198)))
print(manufactured.statistics(DetailedStats(day='1993-01-10', agency=198)))
