from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Tweet
from .serializers import TweetSerializer
from rest_framework import status


def all_tweets(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


def user_tweets(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
        )
