from dataclasses import dataclass
from collections.abc import Sized
from abc import abstractmethod, ABC


class TVShow(ABC):
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

    @abstractmethod
    def synopsis(self):
        pass


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

    def synopsis(self):
        return f"Movie synopsis: {self.__str__()}"

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

    def synopsis(self):
        return f"Series synopsis: {self.__str__()}"


@dataclass
class Documentary:
    name: str
    year: str
    duration: int


class Playlist(Sized):
    @classmethod
    def print(cls, playlist):
        for show in playlist:
            close_statement = f"Movie duration: {show.duration}" if hasattr(show,
                                                                            'duration') else f"Series season: {show.seasons}"
            print(f"{show} {close_statement} :: {type(show)}")

        print("***************************************************************************************")

    def __init__(self, name, shows):
        self.__name = name
        self.__shows = shows

    def __len__(self):
        return len(self.__shows)

    def __getitem__(self, item):
        return self.__shows[item]

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


class PlaylistInheritance(list):
    def __init__(self, name, shows):
        self.__name = name
        super().__init__(shows)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
