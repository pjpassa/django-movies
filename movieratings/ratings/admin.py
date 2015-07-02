from django.contrib import admin
from ratings.models import Link, Rater, Movie, Rating, Tag, Movie_Genre

# Register your models here.
admin.site.register(Rater)
admin.site.register(Link)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Tag)
admin.site.register(Movie_Genre)
