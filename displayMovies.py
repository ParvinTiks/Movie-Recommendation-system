import csv
from random import randint

class Film:
    def __init__(self, title, date, rating, genre, description, cast, language):
        self.title = title
        self.date = date
        self.rating = rating
        self.genre = genre
        self.description = description
        self.cast = cast
        self.language = language
        self.year = date[6:10]


f = open("imdb_movies.csv", "r", encoding = "utf-8")
reader = csv.reader(f)
movies = []

next(reader)

for row in reader:
    movie = Film(row[0], row[1], row[2], row[3], row[4], row[5], row[7], )
    movies.append(movie)


def display(movies, number):
    limit = len(movies)
    usedNumbers = []
    for i in range(number):
        random = randint(0, limit-1)
        while random in usedNumbers:
            random = randint(0, limit)
        usedNumbers.append(random)
        movie = movies[random]
        print(f"{i+1}. {movie.title} ({movie.year}) - rating: {movie.rating}/100 - {movie.genre} - '{movie.description}'")

display(movies, 10)
