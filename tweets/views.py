from django.shortcuts import render
from .models import Tweet


def tweet_list(request):
    # ORM을 사용하여 모든 Tweet 객체를 가져옴
    tweets = Tweet.objects.all()

    # 템플릿에 tweets 리스트를 전달
    return render(request, "tweets/tweet_list.html", {"tweets": tweets})
