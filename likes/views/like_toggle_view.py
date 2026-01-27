from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from likes.models import Like
from posts.models import Post


class LikeToggleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        user = request.user

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        like = Like.objects.filter(user=user, post=post).first()

        if like:
            like.delete()
            return Response({"liked": False}, status=status.HTTP_200_OK)

        Like.objects.create(user=user, post=post)
        return Response({"liked": True}, status=status.HTTP_201_CREATED)