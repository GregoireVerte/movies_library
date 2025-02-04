
class Media:
    """Bazowa klasa dla wszystkich filmów i seriali."""
    def __init__(self, title, release_year, genre, plays=0):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.plays = plays

    def play(self):
        """Zwiększa liczbę odtworzeń o 1."""
        self.plays += 1


class Film(Media):
    """Klasa reprezentująca film."""
    def __str__(self):
        """Zwraca tytuł i rok wydania."""
        return f"{self.title} ({self.release_year})"


class Series(Media):
    """Klasa reprezentująca serial."""
    def __init__(self, title, release_year, genre, season, episode, plays=0):
        super().__init__(title, release_year, genre, plays)
        self.season = season
        self.episode = episode

    def __str__(self):
        """Zwraca tytuł plus SXXEYY."""
        return f"{self.title} S{self.season:02d}E{self.episode:02d}"


# Lista filmów i seriali
library = [
    Film("Pulp Fiction", 1994, "Crime"),
    Film("Inception", 2010, "Sci-Fi"),
    Series("The Simpsons", 1989, "Animation", season=1, episode=4),
    Series("Breaking Bad", 2008, "Drama", season=2, episode=2),
    Film("The Matrix", 1999, "Sci-Fi"),
    Film("The Dark Knight", 2008, "Action"),
    Film("Fight Club", 1999, "Drama"),
    Series("Stranger Things", 2016, "Sci-Fi", season=1, episode=1),
    Series("Game of Thrones", 2011, "Fantasy", season=1, episode=10),
    Series("Friends", 1994, "Comedy", season=2, episode=3)
]


def get_movies(library):
    """Funkcja zwracająca posortowaną listę filmów."""
    movies = [item for item in library if isinstance(item, Film)]
    return sorted(movies, key=lambda x: x.title)


def get_series(library):
    """Funkcja zwracająca posortowaną listę seriali."""
    series = [item for item in library if isinstance(item, Series)]
    return sorted(series, key=lambda x: x.title)











"""
# Testing II
movies = get_movies(library)
print("Filmy:")
for movie in movies:
    print(movie)

print("\nSeriale:")
series = get_series(library)
for serie in series:
    print(serie)
"""


"""
# Testing I
for media in library:
    print(media)

library[0].play()
print(f"'{library[0].title}' odtworzono {library[0].plays} razy.")
"""


