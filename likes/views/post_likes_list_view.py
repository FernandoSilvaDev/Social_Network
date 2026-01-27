from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from likes.models import Like
from likes.serializers import LikeSerializer


class PostLikesListView(ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Like.objects.filter(post_id=self.kwargs["post_id"]).select_related("user")