from django.shortcuts import render_to_response
from ratings.models import Link, Movie, Rating, Movie_Genre, Tag, Rater
from statistics import mean


# Create your views here.
def movie_view(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    ratings = Rating.objects.filter(movie=movie)
    avg_rating = round(movie.average_rating, 1)
    genres = Movie_Genre.objects.filter(movie=movie)
    tags = Tag.objects.filter(id=movie_id)
    link = Link.objects.get(movie=movie)
    context = {"movie": movie, "ratings": ratings, "avg_rating": avg_rating, "tags": tags,
               "genres": genres, "link": link}
    return render_to_response("movies.html", context)


def rater_view(request, rater_id):
    rater = Rater.objects.get(id=rater_id)
    ratings = Rating.objects.filter(rater=rater)
    avg_rating = str(mean([rating.rating for rating in ratings]))[:3]
    tags = Tag.objects.filter(rater=rater)
    context = {"rater": rater, "ratings": ratings, "avg_rating": avg_rating, "tags": tags}
    return render_to_response("raters.html", context)


def top_movie_view(request):
    top_movies = Movie.objects.all().order_by("-average_rating")[:20]
    context = {"top_movies": top_movies}
    return render_to_response("top_movies.html", context)

