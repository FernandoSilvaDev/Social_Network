from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # PATCH /api/v1/notifications/<id>/read/
    @action(detail=True, methods=["patch"])
    def read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({"status": "marked as read"})

    # PATCH /api/v1/notifications/read_all/
    @action(detail=False, methods=["patch"])
    def read_all(self, request):
        qs = Notification.objects.filter(user=request.user, is_read=False)
        qs.update(is_read=True)
        return Response({"status": "all notifications marked as read"})