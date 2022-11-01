from dataclasses import dataclass


class TVShow:
    @staticmethod
    def midia_types():
        return [
            'VIDEO',
            'AUDIO',
            'AUDIOVISUAL',
            'WRITING'
        ]

    midia_type: str = midia_types()[0]

    def __init__(self, name: str, year):
        self.__name = name.title()
        self.__year = year
        self.__likes = 0

    def __str__(self):
        return f"Media name: **{self.__name}** from year **{self.__year}** and, by now, has {self.__likes} likes."

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name.title()

    @property
    def likes(self):
        return self.__likes

    def like_it(self):
        self.__likes += 1

    def dislike(self):
        self.__likes -= 1


class Movies(TVShow):
    def __init__(self, name, year, duration: int):
        super(Movies, self).__init__(name, year)
        self.__duration = duration

    def __str__(self):
        statement = super(Movies, self).__str__()
        statement += f" The duration of movie is **{self.__duration}** minutes."

        return statement

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        if duration < 0:
            raise Exception("No film duration can be less than 0 minutes!!")

        self.__duration = duration


class Series(TVShow):
    def __init__(self, name, year, seasons: int = 1):
        super(Series, self).__init__(name, year)
        self.__seasons = seasons

    def __str__(self):
        statement = super(Series, self).__str__()
        statement += f" The duration of series is **{self.__seasons}** seasons."

        return statement

    @property
    def seasons(self) -> int:
        return self.__seasons

    @seasons.setter
    def seasons(self, seasons: int):
        if seasons < 0:
            raise Exception("No series can have less than 1 season!!")

        self.__seasons = seasons


@dataclass
class Documentary:
    name: str
    year: str
    duration: int


class Playlist:
    @classmethod
    def print(cls, playlist):
        for item in playlist:
            close_statement = f"Movie duration: {item.duration}" if hasattr(item,
                                                                            'duration') else f"Series season: {item.seasons}"
            print(f"{item} {close_statement} :: {type(item)}")

    def __init__(self, name, shows):
        self.__name = name
        self.__shows = shows
        self.__size = shows.__sizeof__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def shows(self):
        return self.__shows

    @shows.setter
    def shows(self, shows):
        self.__shows = shows

    @property
    def size(self):
        return self.__shows.__sizeof__()
