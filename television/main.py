from model import Movies, Series, Playlist, PlaylistInheritance


def simple_like_it():
    avengers.like_it()
    the_office.like_it()
    Playlist.print(shows)


def popular_shows():
    avengers.dislike()
    avengers.dislike()
    avengers.dislike()
    avengers.dislike()
    hannibal.like_it()
    hannibal.like_it()
    hannibal.like_it()
    the_office.like_it()
    the_office.like_it()
    the_office.like_it()
    the_office.like_it()
    the_office.like_it()
    the_office.like_it()
    the_office.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    mounty_python.like_it()
    Playlist.print(shows)


def forced_update_private_methods():
    avengers.name = "XXX XPTO lalala"
    avengers.duration = 200
    the_office.name = "the office - USA"
    Playlist.print(shows)


def playlist_inheritance():
    # Playlist.print(playlist_weekend)
    for s in playlist_weekend:
        print(s)
    print("")
    print(f"name: {playlist_weekend.name} size: {len(playlist_weekend)}. "
          f"{avengers.name} is in playlist? {avengers in playlist_weekend}. "
          f"{fantasia.name} is in playlist? {fantasia in playlist_weekend}")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


if __name__ == "__main__":
    avengers = Movies(name="The Avengers - Infinite War", year="2018", duration=160)
    the_office = Series(name="The Office", year="2010")
    mounty_python = Series(name="mounty python sHow", year="1980", seasons=18)
    hannibal = Movies(name="The Silence os Lambs", year="1990", duration=120)
    fantasia = Movies(name="Fantasia", year="1940", duration=90)
    shows = [avengers, the_office, mounty_python]

    playlist_weekend = PlaylistInheritance(name="Weekend Playlist", shows=[
        avengers,
        the_office,
        mounty_python,
        hannibal
    ])
    # playlist_inheritance()

    playlist_weekday = Playlist(name="Week Day Playlist", shows=[the_office, mounty_python, hannibal, fantasia])
    for show in playlist_weekday.shows:
        print(show)
    print(f"------------------------------------- size: {len(playlist_weekday)} -------------------------------------")

    for show in playlist_weekday:
        print(show)
    print(f"-------------------------------------- len: {len(playlist_weekday)} --------------------------------------")
    print(f"{hannibal.name} is in shows? {hannibal in playlist_weekday.shows}")
    print(f"{avengers.name} is in shows? {avengers in playlist_weekday.shows}")
    print("++++++++++++")

    print(fantasia.synopsis())
    print(the_office.synopsis())

    # simple_like_it()
    # popular_shows()
    # forced_update_private_methods()

    kids_movie = Movies(name="Fantasia", year="1940", duration=90)
    print(".....................................................")
    print(f"Has the movie searched? {playlist_weekday.has_show(kids_movie)}")
    print(".....................................................")

