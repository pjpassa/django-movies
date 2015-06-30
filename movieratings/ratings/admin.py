from django.contrib import admin
from ratings.models import Link, Rater, Movie, Rating, Tag

# Register your models here.
admin.site.register(Rater)
admin.site.register(Link)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Tag)