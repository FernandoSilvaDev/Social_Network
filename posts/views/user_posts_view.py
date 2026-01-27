from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView

from posts.models import Post
from posts.serializers import PostSerializer

User = get_user_model()


class UserPostsView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username = self.kwargs["username"]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError({"detail": "Usuário não encontrado."})

        return (
            Post.objects.filter(author=user)
            .annotate(likes_count=Count("likes", distinct=True), comments_count=Count("comments", distinct=True))
            .order_by("-created_at")
        )