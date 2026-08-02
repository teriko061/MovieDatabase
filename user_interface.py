from movie import Movie
from validation import InputValidator


class MovieDatabase:
    def __init__(self):
        self.movies = [
            Movie("Pulp Fiction", "drama", 1994),
            Movie("Forrest Gump", "drama", 1994),
            Movie("The Godfather", "crime", 1972),
            Movie("Intouchables", "comedy", 2011),
            Movie("Shrek", "animated", 2001),
        ]

    def add(self, movie):
        self.movies.append(movie)

    def list_all(self):
        return self.movies

    def list_by_genre(self, genre):
        genre = genre.lower()
        return [
            film for film in self.movies
            if film.genre.lower() == genre
        ]


class UserInterface:
    def __init__(self):
        self.database = MovieDatabase()
        self.validator = InputValidator()

    def insert_movie(self):
        name = self.validator.enter_name()
        genre = self.validator.enter_genre()
        year = self.validator.enter_year()

        movie = Movie(name, genre, year)
        self.database.add(movie)

        print("\nData saved. Continue selecting an action...")

    def show_list(self):
        movies = self.database.list_all()

        if movies:
            for film in movies:
                print(film)
        else:
            print("\nEvidence is empty.")

    def search_by_genre(self):
        genre = self.validator.enter_genre()
        movies = self.database.list_by_genre(genre)

        if movies:
            for film in movies:
                print(film)
        else:
            print("\nThe specified genre is not in the database.")