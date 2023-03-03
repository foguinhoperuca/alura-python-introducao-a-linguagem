from base_queue import BaseQueue


class NormalQueue(BaseQueue):
    def generate_actual_password(self) -> None:
        self.actual_password = f'PR{self.code}'

    def call_client(self, teller) -> str:
        actual_client = self.queue.pop(0)
        self.customers_served.append(actual_client)

        return f'Actual Client: {actual_client}, go to {teller}'
