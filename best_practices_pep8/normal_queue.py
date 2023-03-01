class NormalQueue:
    code = 0
    queue = []
    customers_served = []
    actual_password = ''

    def generate_actual_password(self) -> None:
        self.actual_password = f'NM{self.code}'

    def reset_queue(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_actual_password()
        self.queue.append(self.actual_password)

    def call_client(self, teller) -> str:
        actual_client = self.queue.pop(0)

        self.customers_served.append(actual_client)

        return f'Actual Client: {actual_client}, go to {teller}'
