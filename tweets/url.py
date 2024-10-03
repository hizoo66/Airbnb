from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/tweets/", views.all_tweets, name="all_tweets"),
    path("api/v1/users/<int:user_id>/tweets/", views.user_tweets, name="user_tweets"),
]
