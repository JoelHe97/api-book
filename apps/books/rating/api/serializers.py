from rest_framework import serializers
from apps.books.models import Rating
from apps.users.api.serializers import UserSerializer


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class RatingDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = ["user", "book"]
