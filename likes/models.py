from django.db import models
from django.contrib.auth.models import User
from tweets.models import Tweet


# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(
        Tweet, on_delete=models.CASCADE, related_name="likes"
    )  # related_name 추가
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "tweet")

    def __str__(self):
        return f"{self.user.username} liked {self.tweet.id}"
