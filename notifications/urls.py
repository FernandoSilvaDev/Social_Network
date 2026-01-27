from rest_framework.routers import DefaultRouter

from .views import NotificationViewSet

# -------------------------------------------------------------------
# Router padrão DRF:
# /api/v1/notifications/
# /api/v1/notifications/<id>/
# -------------------------------------------------------------------
router = DefaultRouter()
router.register("", NotificationViewSet, basename="notifications")

# -------------------------------------------------------------------
# Rotas customizadas via ViewSet actions já definidas:
# PATCH /api/v1/notifications/read_all/ -> read_all()
# PATCH /api/v1/notifications/<id>/read/ -> read()
# -------------------------------------------------------------------
urlpatterns = router.urls