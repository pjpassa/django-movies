from django.shortcuts import render_to_response
from ratings.models import Link, Movie, Rating, Movie_Genre, Tag
from statistics import mean

# Create your views here.
def movie_view(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    ratings = Rating.objects.filter(movie=movie)
    avg_rating = 3 #mean([rating.rating for rating in ratings])
    genres = Movie_Genre.objects.filter(id=movie_id)
    tags = Tag.objects.filter(id=movie_id)
    link = Link.objects.get(id=movie_id)
    context = {"movie": movie, "ratings": ratings, "avg_rating": avg_rating, "tags": tags,
               "genres": genres, "link": link}
    return render_to_response("movies.html", context)
