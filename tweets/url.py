from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweet_list, name="tweet_list"),  # / 경로에 트윗 리스트 보여주기
]
