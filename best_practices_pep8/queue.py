from enum import Enum
from abc import ABCMeta, abstractmethod
from typing import Union, List, TypeVar, Self

from util import NORMAL_QUEUE_TAG, PRIORITY_QUEUE_TAG, DEFAULT_MIN_LENGTH, DEFAULT_MAX_LENGTH
from stats import TypeStats


TBaseQueue = TypeVar("TBaseQueue", bound="BaseQueue")  # FIXME still need it?!


class QueueType(Enum):
    PRIORITY_QUEUE = 0
    NORMAL_QUEUE = 1


class BaseQueue(metaclass=ABCMeta):
    def __init__(self: Self) -> None:
        self._code: int = 0
        self._queue: List[str] = []
        self._customers_served: List[str] = []
        self._actual_password: str = ''

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def queue(self):
        return self._queue

    @property
    def customers_served(self):
        return self._customers_served

    @property
    def actual_password(self):
        return self._actual_password

    @actual_password.setter
    def actual_password(self: TBaseQueue, actual_password: str):
        self._actual_password = actual_password

    @abstractmethod
    def generate_actual_password(self) -> None:
        ...

    @abstractmethod
    def call_client(self, teller: int) -> List:
        ...

    def reset_queue(self) -> None:
        if self.code >= DEFAULT_MAX_LENGTH:
            self.code = DEFAULT_MIN_LENGTH
        else:
            self.code += 1

    def insert_client(self) -> None:
        self.queue.append(self.actual_password)

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_actual_password()
        self.insert_client()


class NormalQueue(BaseQueue):
    def generate_actual_password(self) -> None:
        self.actual_password = f'{NORMAL_QUEUE_TAG}_{self.code:03}'

    def call_client(self, teller: int) -> List:
        display: List[str] = []

        actual_client = self.queue.pop(0)
        self.customers_served.append(actual_client)
        display.append(f'Actual Client: {actual_client}, go to {teller}')

        return display


class PriorityQueue(BaseQueue):
    def generate_actual_password(self) -> None:
        self.actual_password = f'{PRIORITY_QUEUE_TAG}_{self.code:03}'

    def call_client(self, teller: int) -> List:
        display: List[str] = []
        actual_client: str = self.queue.pop(0)
        display.append(f'Client: {actual_client} - Go to Teller {teller}')

        if len(self.queue) > 3:
            display.append(f'Next: {self.queue[0]}')
            display.append(f'Heads up: {self.queue[1]}')

        self.customers_served.append(actual_client)

        return display

    def statistics(self, stats: TypeStats) -> dict:
        return stats.run_stats(customers_served=self.customers_served)


TypeBaseQueue = Union[NormalQueue, PriorityQueue]


class QueueFactory:
    @staticmethod
    def fabricate(type_of_queue: QueueType = QueueType.NORMAL_QUEUE) -> Union[NormalQueue, PriorityQueue]:
        queue: Union[NormalQueue, PriorityQueue, None] = None
        if type_of_queue == QueueType.NORMAL_QUEUE:
            queue = NormalQueue()
        elif type_of_queue == QueueType.PRIORITY_QUEUE:
            queue = PriorityQueue()
        else:
            raise NotImplementedError('Tyope of queue is unknow!!')

        return queue

    @staticmethod
    def fabricate_base_queue(type_of_queue: QueueType = QueueType.NORMAL_QUEUE) -> BaseQueue:
        queue: Union[BaseQueue, None] = None
        if type_of_queue == QueueType.NORMAL_QUEUE:
            queue = NormalQueue()
        elif type_of_queue == QueueType.PRIORITY_QUEUE:
            queue = PriorityQueue()
        else:
            raise NotImplementedError('Tyope of queue is unknow!!')

        return queue
