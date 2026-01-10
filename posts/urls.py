# -------------------------------------------------------------------
# Rotas do app de Posts
# -------------------------------------------------------------------
# Funcionalidades:
# - CRUD de posts via ViewSet
# - Listagem de posts do usuário
# - Curtidas, comentários ou extras podem ser adicionados via actions
# -------------------------------------------------------------------

from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.views.post_view_set import PostViewSet
from posts.views.user_posts_view import UserPostsView

# -------------------------------------------------------------------
# Router padrão DRF (ViewSet de Posts)
# /api/v1/posts/
# /api/v1/posts/<id>/
# -------------------------------------------------------------------
router = DefaultRouter()
router.register("", PostViewSet, basename="posts")

# -------------------------------------------------------------------
# Rotas customizadas
# -------------------------------------------------------------------
urlpatterns = [
    # Lista posts de um usuário específico
    # GET /api/v1/posts/user/<username>/
    path(
        "user/<str:username>/",
        UserPostsView.as_view(),
        name="posts-by-user",
    ),
]

# Inclui rotas CRUD do ViewSet
urlpatterns += router.urls