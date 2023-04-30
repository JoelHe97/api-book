from rest_framework import serializers
from ..models import Book
from apps.books.rating.api.serializers import RatingSerializer, RatingDetailSerializer


class BookSerializer(serializers.ModelSerializer):
    # Adjunta el rating de libros
    ratings = RatingSerializer(many=True, read_only=True, source="rating_set")

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "publisher",
            "image_1",
            "image_2",
            "image_3",
            "ratings",
        ]


class BookTitleUpdateSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True, source="rating_set")

    class Meta:
        model = Book
        fields = ("title", "ratings")
        read_only_fields = ("id", "author", "description")


class BookDetailSerializer(serializers.ModelSerializer):
    ratings = RatingDetailSerializer(many=True, read_only=True, source="rating_set")

    class Meta:
        model = Book
        fields = "__all__"
