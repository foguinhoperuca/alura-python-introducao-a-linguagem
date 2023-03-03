from abc import ABCMeta, abstractmethod


class BaseQueue(metaclass=ABCMeta):
    code: int = 0
    queue: list = []
    customers_served: list = []
    actual_password: str = ''

    @abstractmethod
    def generate_actual_password(self) -> None:
        ...

    @abstractmethod
    def call_client(self, teller) -> list:
        ...

    def reset_queue(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def insert_client(self) -> None:
        self.queue.append(self.actual_password)

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_actual_password()
        self.insert_queue()
