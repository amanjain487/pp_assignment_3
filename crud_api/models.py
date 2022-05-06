from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, null=False)
    objects = UserManager()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, null=False)
    writing_since = models.DateField(default=now)
    speciality_genre = models.ManyToManyField(Genre)
    objects = UserManager()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000, default="No Description Provided")
    price = models.FloatField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=False)
    publish_date = models.DateField(default=now)
    available = models.BooleanField(default=True)
    objects = UserManager()

    def __str__(self):
        return self.name


class RentedBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    phone_no = models.CharField(max_length=10)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    books = models.ManyToManyField(Book)
    objects = UserManager()

    def __str__(self):
        return self.user.name
