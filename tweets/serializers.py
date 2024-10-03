from rest_framework import serializers


class TweetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = serializers.CharField(source="user.username")
    content = serializers.CharField(max_length=280)
    created_at = serializers.DateTimeField()
