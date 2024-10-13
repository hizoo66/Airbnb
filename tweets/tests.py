from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Tweet, User


class TweetAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.tweet = Tweet.objects.create(user=self.user, content="Test tweet")

    def test_get_tweets(self):
        response = self.client.get(reverse("tweet_list_create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_tweet(self):
        data = {"content": "New tweet"}
        response = self.client.post(reverse("tweet_list_create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tweet(self):
        response = self.client.get(
            reverse("tweet_detail", kwargs={"pk": self.tweet.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_tweet(self):
        data = {"content": "Updated tweet"}
        response = self.client.put(
            reverse("tweet_detail", kwargs={"pk": self.tweet.pk}), data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_tweet(self):
        response = self.client.delete(
            reverse("tweet_detail", kwargs={"pk": self.tweet.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
