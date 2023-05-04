from enum import Enum, auto

import mysql.connector


class ScheduleBotStatus(Enum):
    SCHEDULED = auto()
    EXECUTING = auto()
    SUCCESS = auto()
    FAILED = auto()


class DatabaseManager:
    """Access DB from manager to get custom data"""

    class CustomConfOption(Enum):
        SINGLE_CONF = auto()
        MULTIPLE_CONF = auto()

    def __init__(self, settings, logger, lazy=False):
        self._settings = settings
        self._logger = logger
        if not lazy:
            self.connect_with_db()
        else:
            self._connected = False

    @property
    def connected(self):
        return self._connected

    def connect_with_db(self):
        self._db_connection = mysql.connector.connect(
            host=self._settings.db_host,
            user=self._settings.db_user,
            password=self._settings.db_password,
            database=self._settings.db_name
        )
        self._cursor = self._db_connection.cursor(buffered=True)
        self._connected = True

    def get_queue_running_schedule_bot(self, company_id: int, queue_id) -> list:
        scheduled_bots: list = []
        scheduled_bot = None

        if not self._connected:
            self.connect_with_db()

        query = f"""
                SELECT
                    id,
                    bot_module,
                    status
                FROM bot_main_db.scheduler AS s
                WHERE
                    s.status = SCHEDULED AND
                    s.id = '{queue_id}'
                ;"""

        self._cursor.execute(query)
        resultset = self._cursor.fetchall()

        for result in resultset:
            scheduled_bot = [
                result[0],
                result[1],
                result[2]
            ]
            scheduled_bots.append(scheduled_bot)

        return scheduled_bots

    def set_status_queue_running_schedule_bot(self, queue_id: int, status: ScheduleBotStatus) -> None:
        if not self._connected:
            self.connect_with_db()

        query = f"""
                UPDATE bot_main_db.scheduler SET
                    status = '{status.name}',
                    executed = NOW()
                WHERE
                    id = {queue_id}
                ;"""
        self._cursor.execute(query)
        self._db_connection.commit()
        self._logger.debug(f'{self._cursor.rowcount} records affected.')
