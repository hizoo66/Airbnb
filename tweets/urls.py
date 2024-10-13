from django.urls import path
from .views import (
    TweetListCreateAPIView,
    TweetDetailAPIView,
    UserListCreateAPIView,
    UserDetailAPIView,
    UserTweetsAPIView,
    ChangePasswordAPIView,
    LoginAPIView,
    LogoutAPIView,
)

urlpatterns = [
    path("api/v1/tweets/", TweetListCreateAPIView.as_view(), name="tweet_list_create"),
    path("api/v1/tweets/<int:pk>/", TweetDetailAPIView.as_view(), name="tweet_detail"),
    path("api/v1/users/", UserListCreateAPIView.as_view(), name="user_list_create"),
    path("api/v1/users/<int:pk>/", UserDetailAPIView.as_view(), name="user_detail"),
    path(
        "api/v1/users/<int:pk>/tweets/", UserTweetsAPIView.as_view(), name="user_tweets"
    ),
    path(
        "api/v1/users/password/",
        ChangePasswordAPIView.as_view(),
        name="change_password",
    ),
    path("api/v1/users/login/", LoginAPIView.as_view(), name="login"),
    path("api/v1/users/logout/", LogoutAPIView.as_view(), name="logout"),
]
