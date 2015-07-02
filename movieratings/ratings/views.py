from django.shortcuts import render_to_response
from ratings.models import Link

# Create your views here.
def ratings_links(request):
    links = Link.objects.all()
    context = {"links": links}
    return render_to_response("links.html", context)
