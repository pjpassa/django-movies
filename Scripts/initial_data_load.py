import csv
from ratings.models import Rater, Movie, Link, Tag, Rating

raters = set()
with open("../ml-20m/ratings.csv") as file:
    csv_reader = csv.reader(file)

for num, line in enumerate(lines):
    if num == 0:
        continue
    data = line.split(",")
    raters.add(data[0])
    #Rating(user=data[0], movie=data[1], rating=data[2],timestame=data[3]).save()


with open("../ml-20m/tags.csv") as file:
    lines = file.readlines()

for num, line in enumerate(lines):
    if num == 0:
        continue
    data = line.split(",")
    raters.add(data[0])
    #Rating(user=data[0], movie=data[1], tag=data[2],timestame=data[3]).save()

raters = sorted(list(raters))

for rater in raters:
    #Rater(user=rater).save()
    pass
