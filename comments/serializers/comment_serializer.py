from rest_framework import serializers

from comments.models import Comment
from comments.serializers.comment_user_serializer import CommentUserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only=True)
    post_id = serializers.IntegerField(source="post.id", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "post_id", "content", "created_at"]
        read_only_fields = ["id", "created_at", "user", "post_id"]