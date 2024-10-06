from django.urls import path
from .views import (
    AllTweetsAPIView,
    UserTweetsAPIView,
    AllLikesAPIView,
    UserLikesAPIView,
    AllUsersAPIView,
    UserDetailAPIView,
)

urlpatterns = [
    path("api/v1/tweets/", AllTweetsAPIView.as_view(), name="all_tweets"),
    path(
        "api/v1/users/<int:user_id>/tweets/",
        UserTweetsAPIView.as_view(),
        name="user_tweets",
    ),
    path("api/v1/likes/", AllLikesAPIView.as_view(), name="all_likes"),
    path(
        "api/v1/users/<int:user_id>/likes/",
        UserLikesAPIView.as_view(),
        name="user_likes",
    ),
    path("api/v1/users/", AllUsersAPIView.as_view(), name="all_users"),
    path(
        "api/v1/users/<int:user_id>/", UserDetailAPIView.as_view(), name="user_detail"
    ),
]
