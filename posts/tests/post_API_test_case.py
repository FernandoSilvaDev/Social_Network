from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from posts.factories import PostFactory
from users.factories import UserFactory


class PostAPITestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.post = PostFactory(author=self.user)

    def test_list_posts(self):
        response = self.client.get("/api/v1/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        return PostFactory(author=self.user, updated_at=timezone.now())