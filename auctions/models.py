from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    bid_initial = models.DecimalField(max_digits=7, decimal_places=2)
    bids_quantity = models.IntegerField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    active = models.BooleanField()

class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    new_bid = models.DecimalField(max_digits=7, decimal_places=2)

class Comment(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()

class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)