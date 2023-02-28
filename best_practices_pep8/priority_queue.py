class PriorityQueue:
    code:int = 0
    queue:arr = []
    customers_served:arr = []
    actual_password:str = ''

    def generare_actual_password(self) -> None:
        self.actual_password = f'PR{self.code}'

    def reset_queue(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_actual_password()
        self.queue.append(self.actual_password)

    def client_call(self, bank_teller:int) -> str:
        actual_client = self.queue.pop(0)
        self.curstomers_served.append(actual_client)

        return f'Actual client: {actual_client}, go to bank teller {bank_teller}'

    def statistics(self, day:str, agency:str, flag:str) -> dict:
        if flag != 'detail':
            stats = {f'{agency} - {day}\': len(self.customers_served)}'}
        else:
            stats = {}
            stats['day'] = day
            stats['agency'] = agency
            stats['customers served'] = self.customers_served
            stats['total customers served'] = len(self.clientes_atendidos)

        return stats
