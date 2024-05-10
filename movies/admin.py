from django.contrib import admin
from movies.models import Movie , MovieOrder

admin.site.register(Movie)
admin.site.register(MovieOrder)