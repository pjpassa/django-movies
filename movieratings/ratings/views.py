from django.shortcuts import render_to_response
from ratings.models import Links

# Create your views here.
def ratings_links(request):
    links = Links.objects.all()
    context = {"links": links}
    return render_to_response("links.html", context)