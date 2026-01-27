from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from follows.models import Follow
from follows.serializers import FollowSerializer
from users.models import User


class FollowersListView(ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs["user_id"])
        return Follow.objects.filter(following=user).select_related("follower")