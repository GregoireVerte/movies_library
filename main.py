
import random
import datetime

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

    @staticmethod
    def count_episodes(library, title):
        """Metoda statyczna zwracająca liczbę odcinków danego serialu."""
        return sum(1 for item in library if isinstance(item, Series) and item.title == title)



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
    Series("Stranger Things", 2016, "Sci-Fi", season=1, episode=2),
    Series("Stranger Things", 2016, "Sci-Fi", season=1, episode=3),
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


def search(library, search_term):
    """Funkcja wyszukująca po tytule (wielkosc liter bez znaczenia)."""
    search_term = search_term.lower()
    result = [item for item in library if search_term in item.title.lower()]
    return result




def generate_views(library):
    """Funkcja losowo wybiera element z biblioteki i dodaje mu losową liczbę odtworzeń."""
    media_item = random.choice(library)  # Losowo wybiera element
    views_to_add = random.randint(1, 100)  # Losowa liczba odtworzeń w zakresie od 1 - 100
    media_item.plays += views_to_add  # Dodaje losową liczbę odtworzeń
    print(f"'{media_item}' otrzymało {views_to_add} nowych odtworzeń. Razem: {media_item.plays}")


def generate_multiple_views(library, n=10):
    """Funkcja uruchamia generate_views n razy."""
    for _ in range(n):
        generate_views(library)


def top_titles(library, content_type, top_n=5):
    """
    Funkcja zwraca najpopularniejsze tytuły (filmy lub seriale) z biblioteki.
    content_type: Film lub Series
    top_n: liczba najpopularniejszych tytułów (domyślnie 5)
    """
    filtered_content = [item for item in library if isinstance(item, content_type)]
    # Sortowanie elementów według odtworzeń (plays), malejąco (reverse=True)
    sorted_content = sorted(filtered_content, key=lambda x: x.plays, reverse=True)
    return sorted_content[:top_n]


def add_season_to_library(title, release_year, genre, season, num_episodes, library):
    """Dodaje sezon serialu do biblioteki."""
    for episode in range(1, num_episodes + 1):
        library.append(Series(title, release_year, genre, season, episode))







print("Biblioteka filmów \n(Przed dodaniem odtworzeń):")
for media in library:
    print(f"{media}: {media.plays}")


print("\n- Dodanie sezonu 1 'The Office':")
add_season_to_library("The Office", 2005, "Comedy", season=1, num_episodes=6, library=library)


print("\n- Generowanie odtworzeń:")
generate_multiple_views(library, 10)



today = datetime.date.today()
formatted_date = today.strftime("%d.%m.%Y")
print(f"\n- Najpopularniejsze filmy i seriale dnia {formatted_date}.")

print("\nTop 3 filmy:")
top_movies = top_titles(library, Film, top_n=3)
for movie in top_movies:
    print(f"{movie} - {movie.plays} odtworzeń")

print("\nTop 3 seriale:")
top_series = top_titles(library, Series, top_n=3)
for series in top_series:
    print(f"{series} - {series.plays} odtworzeń")



serial_title = "Stranger Things"
print(f"\nLiczba odcinków '{serial_title}' w bibliotece: {Series.count_episodes(library, serial_title)}")










"""
# Testing VII (count_episodes)
serial_title = "Stranger Things"
print(f"Liczba odcinków '{serial_title}' w bibliotece: {Series.count_episodes(library, serial_title)}")
"""




"""
# Testing VI (add_season_to_library)
add_season_to_library("The Office", 2005, "Comedy", season=1, num_episodes=6, library=library)

for media in library:
    print(f"{media}: {media.plays}")
"""



"""
# Testing V
print("Przed dodaniem odtworzeń:")
for media in library:
    print(f"{media}: {media.plays}")

print("\nGenerowanie odtworzeń:")
generate_multiple_views(library, 10)

print("\nTop 4 filmy:")
top_movies = top_titles(library, Film, top_n=4)
for movie in top_movies:
    print(f"{movie} - {movie.plays} odtworzeń")

print("\nTop 4 seriale:")
top_series = top_titles(library, Series, top_n=4)
for series in top_series:
    print(f"{series} - {series.plays} odtworzeń")
"""




"""
# Testing IV
print("Przed dodaniem odtworzeń:")
for media in library:
    print(f"{media}: {media.plays}")

# Uruchamiamy generowanie odtworzeń 10 razy
print("\nGenerowanie odtworzeń:")
generate_multiple_views(library, 10)

# Druk po
print("\nPo dodaniu odtworzeń:")
for media in library:
    print(f"{media}: {media.plays}")
"""




"""
# Testing III
search_result = search(library, "Matrix")
print("Wyniki wyszukiwania 'Matrix':")
for item in search_result:
    print(item)
"""



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


