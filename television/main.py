from model import Movies, Series, Playlist

if __name__ == "__main__":
    avengers = Movies(name="The Avengers - Infinite War", year="2018", duration=160)
    the_office = Series(name="The Office", year="2010")
    mounty_python = Series(name="mounty python sHow", year="1980", seasons=18)
    playlist = [avengers, the_office, mounty_python]

    Playlist.print(playlist)

    avengers.like_it()
    the_office.like_it()
    Playlist.print(playlist)


    avengers.dislike()
    avengers.dislike()
    avengers.dislike()
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
    Playlist.print(playlist)

    avengers.name = "XXX XPTO lalala"
    avengers.duration = 200
    the_office.name = "the office - USA"
    Playlist.print(playlist)
