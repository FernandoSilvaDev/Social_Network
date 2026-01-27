from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

from follows.factories import FollowFactory
from follows.models import Follow
from users.factories import UserFactory


class FollowAPITestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.other_user = UserFactory()

    def test_follow_user(self):
        response = self.client.post(f"/api/v1/users/all-users/{self.other_user.username}/follow/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(
            Follow.objects.filter(
                follower=self.user,
                following=self.other_user,
            ).exists()
        )

    def test_list_follows(self):
        FollowFactory(follower=self.user, following=self.other_user)

        response = self.client.get(f"/api/v1/users/all-users/{self.user.username}/following/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)