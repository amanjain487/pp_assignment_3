from rest_framework import viewsets
from . import models
from . import serializers


class AuthorViewset(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class GenreViewset(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class RentedBooksViewset(viewsets.ModelViewSet):
    queryset = models.RentedBooks.objects.all()
    serializer_class = serializers.RentedBooksSerializer
