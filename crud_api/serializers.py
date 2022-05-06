from rest_framework import serializers
from .models import Book, Genre, Author, RentedBooks


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class RentedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentedBooks
        fields = '__all__'
