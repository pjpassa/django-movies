# Django Movie Ratings

## Description

Create an interface in Django to the [MovieLens dataset][movielens].

## Learning Objectives

After completing this assignment, you should be able to:

### Night 1

* Create a new Django application
* Translate real-world data to Django models
* Explain what a database is
* Explain what a model is
* Use the Django admin
* Structure the Django admin to reflect your data

### Night 2

* Create regular expressions to map URLs to views
* Explain what a view is
* Explain what a template is
* Design simple views
* Use basic HTML
* Extrapolate from basic HTML how to create templates

### Night 3

* Distinguish when to use GET vs POST
* Create forms
* Understand registration and login
* Make use of Django's built in authentication forms and helper
* Extend user objects via OneToOneFields

## Details

### Deliverables

* A Git repo called django-movies containing at least:
  * a `requirements.txt` file
  * a `README.md` file
  * a Django project called `movieratings`

## Night 1

### Normal Mode

Choose a dataset from the [MovieLens dataset options][movielens] and read its
README.

Create a new Django application in the `movieratings` project to hold your
models.

Create Django models for users (call the model `Rater` so as not to
confuse it with Django users), movies, and ratings. Make sure that your models
can contain the data from your dataset.

Create Django admin pages for your models.

[movielens]: http://grouplens.org/datasets/movielens/

### Hard Mode

Start adding methods to your models that you will need later. For `movie`,
you'll want the average rating for each movie, and the ability to get the
top movies by rating.

For `rater`, you'll want the average rating that rater gave to a movie, and
the ability to get the top movies that rater has not seen. You will also want
to be able to find the Euclidean distance between that rater and another using
their movie ratings.

In order to do this, you'll want to [read up on the model layer of Django](https://docs.djangoproject.com/en/1.8/#the-model-layer).

Try to test these new methods. Read [Testing in Django](https://docs.djangoproject.com/en/1.8/topics/testing/)
and then either look at [django-nose](https://pypi.python.org/pypi/django-nose) or [pytest-django](https://pytest-django.readthedocs.org/en/latest/).

## Night 2

### Normal Mode

Using the datamigration method we went over in class. Load in your fixture data from your
datasets into django models.

In your Django application, create views and templates for:

* The top 20 movies rated. This list of movies should have their average rating,
  and each movie listed should have a link to its individual page.

* Each individual movie. This page should have the movie, its average rating,
  and each person who rated it. The list of people should have the rating
  with each person and should have a link to that person's page.

* Each individual user. This page should have their demographic data, and a
  list of all movies they've rated, with the rating they gave it. Each movie
  listed should have the rating they gave it beside it and should have a link
  to that movie's page.

### Hard Mode

Try to build a recommendation algorithm for users in pure python outside of your
django project. We will be putting it into our django project at some point.

## Night 3

### Normal Mode

Link your Rater model to the built-in User model via a OneToOneField. Create
a username, email, and password for all raters.

Add registration, login, and logout to your application.

Add the ability for a user to rate a movie they have not previously rated from
the movie page.

### Hard Mode

Add the ability for a user to edit a rating they've made.

When logged in, customize pages for the user. For example, on the page that
shows the top 20 movies rated, show the user which ones they've rated.

Add a personal page for each user that only they can see. It should have all
their ratings, allow them to edit or delete those ratings, and also show
them the top 20 movies they have not rated.
