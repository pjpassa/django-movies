import csv
from ratings.models import Rater, Movie, Link, Tag, Rating, Movie_Genre


def import_ratings():
    with open("../ml-20m/ratings.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            userId = int(row["userId"])
            movie = Movie.objects.get(id=int(row["movieId"]))
            rating = int(row["rating"])
            timestamp = int(row["timestamp"])
            rater = Rater.objects.get_or_create(rater=userId, id=userId)[0]
            Rating.objects.create(movie=movie, rating=rating, timestamp=timestamp, rater=rater)
    raise BaseException()


def import_tags():
    with open("../ml-20m/tags.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            userId = int(row["userId"])
            movie = Movie.objects.get(id=int(row["movieId"]))
            tag = row["tag"]
            timestamp = int(row["timestamp"])
            tagger = Rater.objects.get_or_create(rater=userId, id=userId)[0]
            Tag.objects.create(movie=movie, tag=tag, timestamp=timestamp, rater=rater)
    raise BaseException()


# This should be run first
def import_movies():
    with open("../ml-20m/movies.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            movieId = int(row["movieId"])
            title = row["title"]
            genres = row["genres"].split("|")
            movie = Movie.objects.create(id=movieId, title=title)
            for genre in genres:
                Movie_Genre.objects.create(movie=movie, genre=genre)
    raise BaseException()


def import_links():
    with open("../ml-20m/links.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            movie = Movie.objects.get(id=int(row["movieId"]))
            imdbId = row["imdbId"]
            tmdbId = row["tmdbId"]
            Link.objects.create(movie=movie, imdb=imdbId, tmdb=tmdbId)