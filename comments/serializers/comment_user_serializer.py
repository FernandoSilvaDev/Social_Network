from rest_framework import serializers

from users.models import User


class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "avatar"]