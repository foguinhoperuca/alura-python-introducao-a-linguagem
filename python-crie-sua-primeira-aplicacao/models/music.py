from typing import Optional, Self


class Music:
    def __init__(self: Self, name: str, artist: str, duration: int) -> None:
        self._name: str = name
        self._artist: str = artist
        self._duration: int = duration

    def __str__(self: Self) -> str:
        return f'name: {self._name} artist: {self._artist} duration: {self._duration}'

    def __repr__(self: Self) -> str:
        return self.__str__()


def music_factory() -> Optional[Music]:
    try:
        name: str = input('Inform the name of music:\n')
        artist: str = input('Inform the name of artist:\n')
        duration: int = int(input('Inform the duration in seconds:\n'))

        return Music(name=name, artist=artist, duration=duration)
    except Exception as e:
        print(f'Could not create music. Error: {e}')
        return None
