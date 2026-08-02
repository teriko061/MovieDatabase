class Movie:
    name = None
    genre = None
    year = None


    def __init__(self, name, genre, year):
        self.name = name
        self.genre = genre
        self.year = year


    def __str__(self):
        return f'{self.name:<50} {self.genre:<20}  {self.year:=4}'
