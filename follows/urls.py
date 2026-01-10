from django.urls import path
from rest_framework.routers import DefaultRouter

from follows.views.followers_list_view import FollowersListView
from follows.views.following_list_view import FollowingListView

router = DefaultRouter()

urlpatterns = [
    # GET /api/v1/follows/<user_id>/followers/
    path(
        "<int:user_id>/followers/",
        FollowersListView.as_view(),
        name="followers-list",
    ),
    # GET /api/v1/follows/<user_id>/following/
    path(
        "<int:user_id>/following/",
        FollowingListView.as_view(),
        name="following-list",
    ),
]

urlpatterns += router.urls