from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from comments.models import Comment
from comments.permissions import IsOwnerOrReadOnly
from comments.serializers.comment_serializer import CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs["post_id"])