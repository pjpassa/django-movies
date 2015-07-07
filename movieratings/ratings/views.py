from datetime import datetime
from statistics import mean
from django.shortcuts import render_to_response
from django.template import RequestContext
from ratings.forms import RatingForm
from ratings.models import Link, Movie, Rating, Movie_Genre, Tag, Rater


# Create your views here.
def movie_view(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    genres = Movie_Genre.objects.filter(movie=movie)
    tags = Tag.objects.filter(id=movie_id)
    link = Link.objects.get(movie=movie)
    if request.POST:
        if "delete" in request.POST:
            Rating.objects.get(movie=movie, rater=request.user.rater).delete()
        else:
            Rating.objects.get_or_create(movie=movie, rater=request.user.rater,
                                         defaults={"rating": request.POST["rating"],
                                                   "timestamp": int(datetime.now().timestamp())})
        movie.calculate_average_rating()
    avg_rating = round(movie.average_rating, 1)
    context = {"movie": movie, "tags": tags, "genres": genres, "link": link, "avg_rating": avg_rating}
    if request.user:
        rating = Rating.objects.filter(movie=movie, rater=request.user.rater)
        context["form"] = RatingForm()
        if rating:
            context["rating"] = rating[0]
            context["form"].rating = rating[0]
    return render_to_response("movies.html", context, context_instance=RequestContext(request))


def rater_view(request, rater_id):
    rater = Rater.objects.get(id=rater_id)
    ratings = Rating.objects.filter(rater=rater)
    avg_rating = str(mean([rating.rating for rating in ratings]))[:3]
    tags = Tag.objects.filter(rater=rater)
    context = {"rater": rater, "ratings": ratings, "avg_rating": avg_rating, "tags": tags}
    return render_to_response("raters.html", context, context_instance=RequestContext(request))


def top_movie_view(request):
    top_movies = Movie.objects.all().order_by("-average_rating")[:20]
    context = {"top_movies": top_movies}
    return render_to_response("top_movies.html", context, context_instance=RequestContext(request))

