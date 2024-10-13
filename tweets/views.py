from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tweet, User
from .serializers import TweetSerializer, UserSerializer
from django.contrib.auth import authenticate, login, logout


class TweetListCreateAPIView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TweetDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            tweet = Tweet.objects.get(pk=pk)
            serializer = TweetSerializer(tweet)
            return Response(serializer.data)
        except Tweet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            tweet = Tweet.objects.get(pk=pk)
            serializer = TweetSerializer(tweet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tweet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            tweet = Tweet.objects.get(pk=pk)
            tweet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tweet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserListCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserTweetsAPIView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            tweets = Tweet.objects.filter(user=user)
            serializer = TweetSerializer(tweets, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ChangePasswordAPIView(APIView):
    def put(self, request):
        user = request.user
        user.set_password(request.data["password"])
        user.save()
        return Response(status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
