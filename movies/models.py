from django.db import models

class RationgChoice(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17= "NC-17"
    

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=RationgChoice.choices,
        default=RationgChoice.G
    )
    synopsis = models.TextField(null=True,default=None)

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='movies'
    )
    orders = models.ManyToManyField(
        'users.User',
        through='movies.MovieOrder',
        related_name='order_movies'
    )



class MovieOrder(models.Model):
    movie = models.ForeignKey(
        'movies.Movie',
        on_delete=models.CASCADE,
        related_name='movie_orders'
    )

    order = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='user_movie_orders'
    )
    
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)