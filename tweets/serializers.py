from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tweet, Like


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Tweet
        fields = ["id", "user", "content", "created_at"]


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    tweet = serializers.CharField(source="tweet.content")

    class Meta:
        model = Like
        fields = ["id", "user", "tweet", "created_at"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
