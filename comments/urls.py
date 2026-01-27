from django.urls import path

from comments.views.comment_detail_view import CommentDetailView
from comments.views.comment_list_create_view import CommentListCreateView

urlpatterns = [
    # /api/v1/posts/<post_id>/comments/
    path(
        "posts/<int:post_id>/comments/",
        CommentListCreateView.as_view(),
        name="post-comments",
    ),
    # /api/v1/posts/<post_id>/comments/<id>/
    path(
        "posts/<int:post_id>/comments/<int:pk>/",
        CommentDetailView.as_view(),
        name="comment-detail",
    ),
]