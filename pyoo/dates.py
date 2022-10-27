from dataclasses import dataclass
import logging


@dataclass
class AluraDate:
    day: str
    month: str
    year: str

    def print_date(self):
        formatted_date = f"{self.day}/{self.month}/{self.year}"

        logging.debug(formatted_date)

        return formatted_date

if __name__ == "__main__":
    dt = AluraDate(26, 10, 2022)
    print(f"{dt=} :: {dt.print_date()=}")
