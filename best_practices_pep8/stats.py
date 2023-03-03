import logging
from typing import List, Dict, Union
from abc import ABCMeta, abstractmethod


class Stats(metaclass=ABCMeta):
    def __init__(self, day: str, agency: int) -> None:
        self._day: str = day
        self._agency: int = agency

    @property
    def day(self):
        return self._day

    @property
    def agency(self):
        return self._agency

    @abstractmethod
    def run_stats(self, customers_served: List[str]) -> dict:
        ...


class ResumedStats(Stats):
    def run_stats(self, customers_served: List[str]) -> dict:
        stats: Dict[str, Union[str, int, List[str]]] = {}

        logging.info(f'{customers_served=}')
        stats[f'{self.agency}_{self.day}'] = len(customers_served)

        return stats


class DetailedStats(Stats):
    def run_stats(self, customers_served: List[str]) -> dict:
        stats: Dict[str, Union[str, int, List[str]]] = {}

        logging.info(f'{customers_served=}')
        stats['day'] = self.day
        stats['agency'] = self.agency
        stats['customers served'] = customers_served
        stats['total customers served'] = len(customers_served)

        return stats


TypeStats = Union[ResumedStats, DetailedStats]
