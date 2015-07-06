"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from ratings.views import movie_view, rater_view, top_movie_view

urlpatterns = [
    url(r'^register/', CreateView.as_view(template_name='register.html',
                                             form_class=UserCreationForm,
                                             success_url='/')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', top_movie_view, name="top_movies"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movie/(?P<movie_id>\d+)', movie_view, name="movie"),
    url(r'^rater/(?P<rater_id>\d+)', rater_view, name="rater"),
]
