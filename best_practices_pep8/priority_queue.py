from base_queue import BaseQueue


class PriorityQueue(BaseQueue):
    def generate_actual_password(self) -> None:
        self.actual_password = f'PR{self.code}'

    def call_client(self, teller) -> list:
        display = []
        actual_client = self.queue.pop(0)
        display.append(f'Client: {actual_client} - Teller {teller}')

        if len(self.queue) > 3:
            display.append(f'Next: {self.queue[0]}')
            display.append(f'Heads up: {self.queue[1]}')

        self.customers_served.append(actual_client)

        return display

    def statistics(self, day: str, agency: int, flag: str) -> dict:
        if flag != 'detail':
            stats = {f'{agency} - {day}': len(self.customers_served)}
        else:
            stats = {}
            stats['day'] = day
            stats['agency'] = agency
            stats['customers served'] = self.customers_served
            stats['total customers served'] = len(self.customers_served)

        return stats
