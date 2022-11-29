import logging
from datetime import datetime, timedelta


class DateBr:
    UNIVERSAL_PATTERN = "%Y-%m-%dT%H:%M:%S"
    BRAZILIAN_PATTERN = "%d/%m/%Y %H:%M:%S"
    YEAR_MONTH = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december"
    ]

    WEEK_DAYS = [
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY"
    ]

    def __init__(self):
        self._register_datetime = datetime.today()

    def __str__(self):
        return self.format(fmt_type="BR")



    @property
    def register_datetime(self):
        return self._register_datetime

    def format(self, fmt_type=""):
        fmt = DateBr.UNIVERSAL_PATTERN
        if fmt_type == "BR":
            fmt = DateBr.BRAZILIAN_PATTERN

        logging.debug(f"Format type choosen was {fmt = } from {fmt_type = }")
        return self._register_datetime.strftime(fmt)

    def since(self):
        return datetime.now() - self._register_datetime

    def month(self):
        return DateBr.YEAR_MONTH[self._register_datetime.month - 1]

    def weekday(self):
        return DateBr.WEEK_DAYS[self._register_datetime.weekday()]
