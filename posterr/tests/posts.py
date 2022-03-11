from django.test import TestCase
from posterr.models import Post, User


class PostTest(TestCase):

    def setUp(self):
        john = User.objects.create(
            name="John Doe", username="johndoe")
        Post.objects.create(
            poster=john, content="Just a regular post")
        Post.objects.create(
            poster=john, content="Just another regular post")

    def test_count_post_from_user(self):
        user = User.objects.get(username='johndoe')
        johnsposts = Post.objects.filter(poster=user)
        self.assertEqual(
            johnsposts.count(), 2)